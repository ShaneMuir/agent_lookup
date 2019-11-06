from app import app


@app.route('/')
def hello_world():
    print(app)
    return 'Hello, World!'