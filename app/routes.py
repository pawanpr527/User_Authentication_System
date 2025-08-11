from flask import Blueprint, render_template, redirect, url_for, flash
from app.form import RegistrationForm, LoginForm
from app.models import User
from app.extensions import db  # ✅ FIXED
from flask_login import login_user, logout_user, login_required, current_user
from flask import after_this_request
bp = Blueprint("main", __name__)

@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been Log out.")
    return redirect(url_for('main.login'))
@bp.route('/Bio')
@login_required
def Bio():
   @after_this_request
   def addheader(response):
       response.headers['Cache-Control'] = "no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0"
       response.headers["Pragma"] = "no-cache"
       response.headers['Expires'] = "0"
       return response
   return render_template('Bio.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if user and user.password == password:
            login_user(user)
            flash("Login Success", 'success')
            return redirect(url_for('main.Bio'))
        else:
            flash("Enter valid Email or Password", 'danger')
    return render_template('login.html', form=form)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        exit_user = User.query.filter_by(username=form.username.data).first()
        exit_email = User.query.filter_by(email=form.email.data).first()

        if exit_user or exit_email:
            flash("User already exists with Email or Username", 'danger')
            return redirect(url_for('main.register'))

        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created. Please log in.', 'success')
        return redirect(url_for('main.login'))

    return render_template('register.html', form=form) 
