from mysqlconnection import connectToMySQL
import random

SCHEMA = 'november_ninja_gold'

def create_activity(user_id, location_id, gold):
  db = connectToMySQL(SCHEMA)
  query = 'INSERT INTO activities (user_id, location_id, gold_amount, created_at, updated_at) VALUES (%(user)s, %(location)s, %(gold_amount)s, NOW(), NOW());'
  data = {
    'user': user_id,
    'location': location_id,
    'gold_amount': gold
  }
  db.query_db(query, data)

def calculate_gold(location_id):
  db = connectToMySQL(SCHEMA)
  query = 'SELECT min_gold, max_gold FROM locations WHERE id = %(id)s;'
  data = {
    'id': location_id
  }
  location_list = db.query_db(query, data)
  location = location_list[0]
  gold = random.randint(location['min_gold'], location['max_gold'])
  return gold

def get_current_gold(user_id):
  db = connectToMySQL(SCHEMA)
  query = 'SELECT gold FROM users WHERE id = %(user)s;'
  data = {
    'user': user_id
  }
  user_list = db.query_db(query, data)
  user = user_list[0]
  current_gold = user['gold']
  return current_gold

def update_user_gold(user_id, gold):
  db = connectToMySQL(SCHEMA)
  query = 'UPDATE users SET gold = %(gold_amount)s WHERE id = %(user)s;'
  data = {
    'gold_amount': gold,
    'user': user_id
  }
  db.query_db(query, data)

def validate_location(form):
  errors = []

  if len(form['name']) < 1:
    errors.append("Location must have a name")
  
  try:
    min_gold = int(form['min_gold'])
  except:
    errors.append('Min Gold must be an integer')

  try:
    max_gold = int(form['max_gold'])
  except:
    errors.append('Max Gold must be an integer')

  if not errors:
    if min_gold > max_gold:
      errors.append("Max Gold must be greater than Min Gold")
  
  return errors

def create_location(form):
  db = connectToMySQL(SCHEMA)
  query = 'INSERT INTO locations (name, min_gold, max_gold, created_at, updated_at) VALUES (%(name)s, %(min_gold)s, %(max_gold)s, NOW(), NOW());'
  data = {
    'name': form['name'],
    'min_gold': int(form['min_gold']),
    'max_gold': int(form['max_gold']),
  }
  db.query_db(query, data)