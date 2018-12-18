from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Comment

# Create your views here.
def create(req):
  errors = Comment.objects.validate(req.POST, req.session['user_id'])
  if errors:
    for error in errors:
      messages.error(req, error)
  else:
    Comment.objects.create_comment(req.POST, req.session['user_id'])
  return redirect('tickets:show', ticket_id = req.POST['ticket'])