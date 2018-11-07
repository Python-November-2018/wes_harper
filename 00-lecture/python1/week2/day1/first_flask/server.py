from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
  my_list = ["one", "two", "three"]
  for i in range(len(my_list)):
    my_list[i] += "hi"
  print(my_list)

  return render_template('index.html', color="Orange", my_list = my_list)

@app.route('/other')
def other():
  return render_template('other.html')

@app.route('/process', methods=["POST"])
def process():
  print("*" * 80)
  print(request.form)
  print("*" * 80)
  return redirect('/')

if __name__ == "__main__":
  app.run(debug=True)