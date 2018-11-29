from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
def index(req):
  return render(req, 'main/index.html')

def success(req):
  context = {
    "title": "Success Page"
  }
  return render(req, 'main/success.html', context)

def colors(req, color):
  context = {
    "color": color
  }
  return render(req, 'main/colors.html', context)

def process(req):
  errors = []

  if len(req.POST['name']) < 2:
    errors.append('Name must be at least 2 characters')
  
  if len(req.POST['email']) < 5:
    errors.append('Email must be valid')

  if len(errors) > 1:
    for error in errors:
      messages.error(req, error)
    return redirect('/')

  return redirect('/success')