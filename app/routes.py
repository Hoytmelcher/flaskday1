from flask import render_template
from app import app


@app.route('/')
def index():
    return render_template('index.jinja', title='Home')

@app.route('/about')
def about():
    return render_template('about.jinja')

@app.route('/register')
def register():
    return render_template('register.jinja')

@app.route('/login')
def login():
    return render_template('login.jinja')

@app.route('/blog')
def blog():
    return render_template('blog.jinja')