from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
from forms import LoginForm, Registration
from .. import db
from ..models import User


@auth.route('/register', methods=['GET', 'POST'])
def sign_up():
    form = Registration()
	if form.validate_on_submit():
		user = User(first_name = form.first_name.data,
					last_name = form.last_name.data,
					email = form.email.data,
					username = form.username.data,
					password = form.password.data,
					confirm = form.confirm.data
					)
		db.session.add(user)
		db.session.commit()
		flash('Thank you for registering')
		return redirect(url_for('auth.sign_in'))
	return render_template("auth/register.html", form=form, title="Sign Up")


@auth.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for('home.dashboard'))
        else:
            flash('Invalid email or password.')
    return render_template('auth/sign_in.html', form=form, title='Sign In')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('auth.sign_in'))