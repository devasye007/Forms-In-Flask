from app import app                     # ✅ Import your Flask app instance
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm        # ✅ Import the LoginForm

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('login'))   # or '/index' if you have that route
    return render_template('login.html', title='Sign In', form=form)
from flask import render_template

@app.route('/')
def home():
    return render_template('base.html', title='Home')
