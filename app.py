from flask import Flask
app = Flask(__name__)

@app.route('/')
def main():
    return 'Hello, world!'

@app.route('/homepage')
def home():
    return f"This is your homepage :) "

if __name__ == '__main__':
    app.run(debug=True)