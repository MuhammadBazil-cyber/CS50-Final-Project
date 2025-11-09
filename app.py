from flask import Flask, flash, redirect, render_template, request, session, url_for    
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
import bcrypt
from flask_mysqldb import MySQL
import MySQLdb
# from functools import wraps # not used currently but can be useful for decorators

app = Flask(__name__)

# my sql configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'mydatabase'
app.secret_key = 'your_secret_key'
 
#  Think of SQL as the language you use to talk to a database.
# Think of MySQL as a specific software program (a type of database) that understands and executes commands written in SQL.
mysql = MySQL(app)  

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()]) 
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()]) 
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)  # <-- FIXED!
        cursor.execute('SELECT * FROM cs50 WHERE email = %s', (email,))
        existing_user = cursor.fetchone()
        
        if existing_user:
            flash('Email already registered', 'danger')
            return redirect(url_for('login'))

        cursor.execute('INSERT INTO cs50 (name, email, password) VALUES (%s, %s, %s)', 
                       (name, email, password,))
        mysql.connection.commit()
        cursor.close()
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/add_income', methods=['POST'])
def add_income():
    if 'logged_in' in session:
        amount = request.form.get('amount')

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('UPDATE cs50 SET amount = amount + %s WHERE id = %s',
                       (amount, session['user_id']))
        mysql.connection.commit()
        cursor.close()
        flash('Income added successfully!', 'success')
        return redirect(url_for('home'))
    else:
        flash('Please log in to access this page.', 'warning')
        return redirect(url_for('login'))

@app.route('/home')
def home():
    if 'logged_in' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT amount FROM cs50 WHERE id = %s',
                       (session['user_id'],))
        income = cursor.fetchone()
        finalamount = income['amount']
        cursor.close()
        return render_template('home.html', finalamount=finalamount)
    else:
        flash('Please log in to access this page.', 'warning')
        return redirect(url_for('login'))
    
@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)  # <-- FIXED!
        cursor.execute('SELECT * FROM cs50 WHERE email = %s', (email,))
        user = cursor.fetchone()
        cursor.close()
        if user and password == user['password']:
            session['logged_in'] = True
            session['user_id'] = user['id']
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)            
