from tempfile import template

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return 'Hello, world!'

@app.route('/homepage')
def home():
    return f"This is your homepage :) "

@app.route('/resume')
def get_resume():
    return render_template("resume.html", page_title="Моє резюме")

if __name__ == '__main__':
    app.run(debug=True)