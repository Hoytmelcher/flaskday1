from flask import render_template, flash, redirect
from app import app
from app.forms import RegisterForm, LoginForm, CarForm
from app.models import User, Listing
from flask_login import current_user, login_user, logout_user, login_required


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
        username = form.username.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        password = form.password.data
        u = User(username=username,email=email,first_name=first_name,last_name=last_name,password_hash='')
        user_match = User.query.filter_by(username=username).first()
        email_match = User.query.filter_by(email=email).first()
        if user_match:
            flash(f'Username {username} already exists, try again')
            return redirect('/register')
        elif email_match:
            flash(f'Email {email} already in use, try again')
            return redirect('/register')
        else:
            u.hash_password(password)
            u.commit()
        flash(f'Request to register {username} sucessful')
        return redirect('/')
    return render_template('register.jinja', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user_match = User.query.filter_by(email=email).first()
        if not user_match or not user_match.check_password(password):
            flash(f'Email or password was incorrect, try again')
            return redirect('/login')
        flash(f'Welcome back')
        login_user(user_match, remember=form.remember_me.data)
        return redirect('/')
    return render_template('login.jinja', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

@app.route('/blog')
def blog():
    return render_template('blog.jinja')

@app.route('/cars', methods=['GET', 'POST'])
def cars():
    form = CarForm()
    if form.validate_on_submit():
        make = form.make.data
        model = form.model.data
        year = form.year.data
        color = form.color.data
        price = form.price.data
        user_id = current_user.id
        l = Listing(make=make,model=model,year=year,color=color,price=price,user_id=user_id)
        l.commit() 
        flash(f'{form.year.data} {form.make.data} {form.model.data} registered')
        return redirect('/cars')
    return render_template('cars.jinja', form=form)