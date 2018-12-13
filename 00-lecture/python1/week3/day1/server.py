from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = "as;dlkjasdfkjsdflkjasdfasd"

@app.route('/')
def index():
  db = connectToMySQL('november_ninja_gold')
  user_list = db.query_db('SELECT * FROM users;')
  return render_template('index.html', users = user_list)

if __name__ == "__main__":
  app.run(debug = True)