from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates')

todos = []

@app.route('/')
def index():
    pass
    # return render_template(template_name_or_list: 'index.html', todos=todos)
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    todo = request.form['todo']
    todos.append({'task': todo, 'done': False})
    return redirect(url_for('index'))

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    todo = todos[index]
    if request.method == "POST":
        todo['task'] = request.form['todo']
        return redirect(url_for('index'))
    else:
        return render_template('edit.html', todo = todo, index = index)
    



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)