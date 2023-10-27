from flask import Blueprint, render_template, request, flash, redirect, url_for, session, Flask
from .models import User, Contact
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/ecommerce/templates/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('auth.cart'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/ecommerce/templates/signup.html', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
      
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(password) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email,  password=generate_password_hash(
                password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Congratulations!, Account created', category='success')
            return redirect(url_for('auth.login'))

    return render_template("signup.html", user=current_user)

@auth.route('/ecommerce/templates/about.html')
def about():
    return render_template('about.html')


@auth.route('/ecommerce/templates/index.html')
def index():
    return render_template('index.html')


@auth.route('/ecommerce/templates/contact.html', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        if not name or not email or not message:
            flash('Please fill in all fields.', category='error')
        elif len(message) < 4:
            flash('Message must be greater than 3 characters.', category='error')
        else:
            new_message = Contact(name=name, email=email, message=message)
            db.session.add(new_message)
            db.session.commit()
            flash('Thank you for contacting us. We will respond as soon as possible!', category='success')
            return redirect(url_for('auth.contact'))  

    return render_template('contact.html')


@auth.route('/ecommerce/templates/bundles.html')
def bundles():
    return render_template('bundles.html')


@auth.route('/ecommerce/templates/bodyLotion.html')
def bodyLotion():
    return render_template('bodyLotion.html')


@auth.route('/ecommerce/templates/cleanser.html')
def cleanser():
    return render_template('cleanser.html')


@auth.route('/ecommerce/templates/moisturisers.html')
def moisturisers():
    return render_template('moisturisers.html')


@auth.route('/ecommerce/templates/sunscreen.html')
def sunscreen():
    return render_template('sunscreen.html')


@auth.route('/ecommerce/templates/shop.html')
def shop():
    return render_template('shop.html')


@auth.route('/ecommerce/templates/cart.html')
@login_required
def cart():
    return render_template('cart.html', user=current_user)