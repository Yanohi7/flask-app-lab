from flask import Flask, request

app = Flask(__name__)


@app.route('/')  # URL '/' to be handled by main() route handler
def main():
    return 'Hello, world!'


@app.route('/homepage')
def home():
    """View for the Home page of your website."""
    agent = request.user_agent
    return f"<h1>This is your homepage :) - {agent}</h1> "


@app.route('/hi/<string:name>/<int:age>')
def greetings(name, age):
    name = name.upper()
    year = 2024 - age
    return f"Welcome {name=} {year=}"


if __name__ == "__main__":
    app.run()  # Launch built-in web server and run this Flask webapp, debug=True


