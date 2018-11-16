from flask import Flask, render_template, redirect, session, request, flash
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
SCHEMA = 'november_ninja_gold'

app = Flask(__name__)
app.secret_key = "asdfasdfasdfasdfasdfasdfasdfasdf"
bcrypt = Bcrypt(app)

@app.route('/')
def index():
  if 'user_id' not in session:
    return redirect('/users/new')

  return render_template('index.html')

@app.route('/users/new')
def login_page():
  return render_template('login_reg.html')

@app.route('/users/create', methods=['POST'])
def create_user():
  errors = False

  # check if username is long enough
    # if so, check for uniqueness
  if len(request.form['username']) < 3:
    flash('Username must be at least 3 characters long.')
    errors = True
  else:
    db = connectToMySQL(SCHEMA)
    query = 'SELECT id FROM users WHERE username = %(username)s;'
    data = {
      'username': request.form['username']
    }
    matching_users = db.query_db(query, data)
    if len(matching_users) > 0:
      flash("Username already in use.")
      errors = True

  # check if email is valid
    # if so, check for uniqueness
  if not EMAIL_REGEX.match(request.form['email']):
    flash("Email must be valid")
    errors = True
  else:
    db = connectToMySQL(SCHEMA)
    query = 'SELECT id FROM users WHERE email = %(email)s;'
    data = {
      'email': request.form['email']
    }
    matching_users = db.query_db(query, data)
    if len(matching_users) > 0:
      flash("Email already in use")
      errors = True

  # check if password is long enough
  if len(request.form['password']) < 8:
    flash("Password must be at least 8 characters long")
    errors = True

  # check if password matches confirm
  if request.form['password'] != request.form['confirm']:
    flash("Passwords must match")
    errors = True

  if errors == True:
    return redirect('/users/new')
  else:
    # create user and log them in
    db = connectToMySQL(SCHEMA)
    query = 'INSERT INTO users (username, email, pw_hash, gold, created_at, updated_at) VALUES(%(username)s, %(email)s, %(pw_hash)s, 0, NOW(), NOW())'
    data = {
      'username': request.form['username'],
      'email': request.form['email'],
      'pw_hash': bcrypt.generate_password_hash(request.form['password'])
    }
    user_id = db.query_db(query, data)
    session['user_id'] = user_id
    return redirect('/')

@app.route('/logout')
def logout():
  session.clear()
  return redirect('/users/new')

if __name__ == "__main__":
  app.run(debug=True)