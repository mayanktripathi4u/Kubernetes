# Run the App
```bash
python app.py
```
or
```bash
flask run
```

when you use the `flask run` command, it ignores the settings (`port`) you defined in `app.py`. This happens because flask run starts the application based on environment variables and not the Python script directly.

To make Flask run on port 8000 when using the flask run command, you need to set the `FLASK_RUN_PORT` environment variable. Here’s how you can do it:

On Linux/macOS (Bash):
```bash 
export FLASK_RUN_PORT=8000
echo $FLASK_RUN_PORT
flask run
```

Alternatively:
You can specify the port directly in your terminal when you run Flask:
```bash
flask run --port 8000
```
Both methods will make sure Flask runs on port 8000, regardless of what’s specified in the app.py script.


