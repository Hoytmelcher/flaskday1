from flask import render_template, flash, redirect
from app import app
from app.forms import RegisterForm, LoginForm, CarForm

@app.route('/')
def index():
    return render_template('index.jinja', title='Home')

@app.route('/about')
def about():
    return render_template('about.jinja')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'Request to register {form.username} sucessful')
        return redirect('/')
    return render_template('register.jinja', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Welcome back')
        return redirect('/')
    return render_template('login.jinja', form=form)

@app.route('/blog')
def blog():
    return render_template('blog.jinja')

@app.route('/cars', methods=['GET', 'POST'])
def cars():
    form = CarForm()
    return render_template('cars.jinja', form=form)