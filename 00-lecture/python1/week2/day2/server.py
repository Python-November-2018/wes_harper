from flask import Flask, render_template, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = "asdflkajsd;lkasdfkkelflkjsasdflfkfj;lwqeoijzvwe"

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
  # BAD CODE
  # NEVER DO THIS
  # username = request.form['username']
  # return render_template('success.html', user=username)

  # GOOD CODE
  errors = False
  if len(request.form['username']) < 2:
    print("USERNAME VALIDATION FAILED")
    errors = True

  if len(request.form['password']) < 8:
    print('PASSWORD VALIDATION FAILED')
    errors = True

  if errors == True:
    return redirect('/')

  session['username'] = request.form['username']
  session['password'] = request.form['password']
  return redirect('/success')

@app.route('/success')
def success():
  return render_template('success.html')

@app.route('/variables/<color>/<num>')
def variables(color, num):
  return render_template('variables.html', title="Variables Page", col=color, number=num)

if __name__ == "__main__":
  app.run(debug=True)