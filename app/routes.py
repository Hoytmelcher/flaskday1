from flask import render_template
from app import app
from app.forms import RegisterForm, LoginForm, CarForm

@app.route('/')
def index():
    return render_template('index.jinja', title='Home')

@app.route('/about')
def about():
    return render_template('about.jinja')

@app.route('/register')
def register():
    form = RegisterForm()
    return render_template('register.jinja', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.jinja', form=form)

@app.route('/blog')
def blog():
    return render_template('blog.jinja')

@app.route('/cars')
def cars():
    form = CarForm()
    return render_template('cars.jinja', form=form)