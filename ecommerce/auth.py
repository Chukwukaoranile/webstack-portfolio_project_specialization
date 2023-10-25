from flask import Blueprint, render_template, request, flash, redirect, url_for, session, Flask
from .models import User, Cart
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
                return redirect(url_for('views.home'))
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


@auth.route('/ecommerce/templates/sign_up.html', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.index'))

    return render_template("sign_up.html", user=current_user)

@auth.route('/ecommerce/templates/about.html')
def about():
    return render_template('about.html')


@auth.route('/ecommerce/templates/index.html')
def index():
    return render_template('index.html')

@auth.route('/ecommerce/templates/contact.html')
def contact():
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


@auth.route('/add_to_cart/<int:product_id>/<int:quantity>', methods=['POST'])
def add_to_cart(product_id, quantity):
    product = get_product_by_id(product_id)  # Fetch product details from the database
    if product is not None:
        cart_item = {
            'product_id': product_id,
            'quantity': quantity,
            'price': product.price,  # Store the product's price in the cart
        }
        cart.append(cart_item)  # Add the item to the cart
        session['cart'] = cart  # Update the cart in the session
    return redirect(url_for('product_detail', product_id=product_id))

@auth.route('/cart')
def view_cart():
    # Retrieve the cart items from your database
    cart = {
    'item1': {'quantity': 2, 'price': 10.0},
    'item2': {'quantity': 1, 'price': 5.0},
    'item3': {'quantity': 3, 'price': 8.0}
}
 

    # Define a function to calculate the total price
    def calculate_cart_total(cart):
        total = 0
        for product_id, item in cart.items():
            total += item['price'] * item['quantity']
            return total 

    # Add the calculate_cart_total function to the template context
    return render_template('cart.html', cart=cart, calculate_cart_total=calculate_cart_total)
'''
@auth.route('/cart', methods=['GET'])
def view_cart():
    # Retrieve the user's cart from the session
    cart = session.get('cart', {})

    # You can fetch product details based on the product IDs stored in the cart

    # Render a template to display the cart
    return render_template('cart.html', cart=cart)

    def calculate_cart_total(cart):
        total = 0
        for item in cart:
            total += item['price'] * item['quantity']
            return total
'''
