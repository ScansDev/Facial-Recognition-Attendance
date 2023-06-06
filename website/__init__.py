from flask import Flask

def create_app():
    app = Flask()
    app.config['SECRET_KEY'] = '903685aA!'
    return app