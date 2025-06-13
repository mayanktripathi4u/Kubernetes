import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tempfile
from io import BytesIO
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
import os
import socket

def detect_environment():
    if os.getenv("KUBERNETES_SERVICE_HOST"):
        return "Running inside Kubernetes ☸️"
    elif os.path.exists("/.dockerenv"):
        return "Running inside Docker 🐳 "
    elif "localhost" in socket.gethostname() or "local" in socket.gethostname():
        return "Running locally 🏠 "
    else:
        return "Environment unknown ❓"
    

# Load dataset
iris = load_iris()
x = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target
labels = iris.target_names

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=99)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
report = classification_report(y_test, y_pred, target_names=labels)
conf_matrix = confusion_matrix(y_test, y_pred)
accoracy = model.score(X_test, y_test)

# Streamlit app
st.set_page_config(page_title="Iris Dataset Classification", layout="wide")
st.title("Iris Dataset Classification")

# Show Raw Data
if st.checkbox("Show Raw Data"):
    st.subheader("Raw Data")
    # st.dataframe(x)
    st.write(x)

# Model Summary
model_summary = f"""
Model: Random Forest Classifier
Training Set Size: {len(X_train)}
Test Set Size: {len(X_test)}
Model Accuracy: {accoracy:.2f}
"""

st.subheader("Model Summary")
# st.write(model_summary)
st.text(model_summary)

# Classification Report
st.subheader("Classification Report")
st.text(report)

# Confusion Matrix
st.subheader("Confusion Matrix")
fig_cm, ax_cm = plt.subplots()
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels, ax=ax_cm)
st.pyplot(fig_cm)

# Feature Importance Plot
st.subheader("Feature Importance")
importances = model.feature_importances_
fig_fi, ax_fi = plt.subplots()
pd.Series(importances, index=x.columns).sort_values(ascending=False).plot(kind='barh', color="teal", ax=ax_fi)
st.pyplot(fig_fi)

# Sidebar Input
st.sidebar.info(f"🧠 App Status: {detect_environment()}")
st.sidebar.info(f"🧠 Hostname: {socket.gethostname()}")

st.sidebar.header("Predict New Sample Data")
sepal_length = st.sidebar.slider("Sepal Length (cm)", float(x.min()[0]), float(x.max()[0]), float(x.mean()[0]))
sepal_width = st.sidebar.slider("Sepal Width (cm)", float(x.min()[1]), float(x.max()[1]), float(x.mean()[1]))
petal_length = st.sidebar.slider("Petal Length (cm)", float(x.min()[2]), float(x.max()[2]), float(x.mean()[2]))
petal_width = st.sidebar.slider("Petal Width (cm)", float(x.min()[3]), float(x.max()[3]), float(x.mean()[3]))

new_sample = [[sepal_length, sepal_width, petal_length, petal_width]]
prediction = model.predict(new_sample)
st.sidebar.success(f"Predicted Class: {labels[prediction[0]]}")

# Video
st.subheader("Video")
st.video("https://www.youtube.com/watch?v=2z6g8c7b1a4", start_time=0)


# Generate PDF Report
def generate_pdf_with_plot(report_text, model_summary, fig_cm, fig_fi):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # ---- Page 1 ----
    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(30, height - 50, "Iris Dataset Classification Report")

    # Model Summary
    text = c.beginText(40, height - 40)
    text.setFont("Helvetica-Bold", 12)
    text.textLines("Model Summary:")
    text.setFont("Helvetica", 10)
    for line in model_summary.split('\n'):
        text.textLine(line)
    c.drawText(text)

    # c.setFont("Helvetica", 12)
    # c.drawString(30, height - 100, "Model Summary:")
    # c.drawString(30, height - 120, model_summary)

    # Classification Report
    # c.drawString(30, height - 160, "Classification Report:")
    # text_object = c.beginText(30, height - 180)
    # text_object.setFont("Helvetica", 10)
    # for line in report_text.split('\n'):
    #     text_object.textLine(line)
    # c.drawText(text_object)

    # # Confusion Matrix Plot
    # cm_image = ImageReader(fig_cm)
    # c.drawImage(cm_image, 30, height - 400, width=500, height=200)

    # # Feature Importance Plot
    # fi_image = ImageReader(fig_fi)
    # c.drawImage(fi_image, 30, height - 650, width=500, height=200)

    c.showPage()

    c.save()
    
    buffer.seek(0)
    return buffer

# PDF Export Button
if st.button("Download PDF Report"):
    pdf = generate_pdf_with_plot(report, model_summary, fig_cm, fig_fi)
    st.download_button("Download PDF", pdf, file_name="iris_classification_report.pdf", mime="application/pdf")

# Run the Streamlit app
# Use the command `streamlit run app.py` to run the app

