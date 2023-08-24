from flask import Flask

def create_app():
    app = Flask(__name__)
    with open('.secret_key', 'r') as f: 
        app.config['SECRET_KEY'] =  f.read().strip()
    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app