from flask import Flask
from posts.views import postsbp
from users.views import user_bp

def create_app():
    app = Flask(__name__)

    # Реєстрація блюпринтів
    app.register_blueprint(posts_bp)
    app.register_blueprint(user_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
