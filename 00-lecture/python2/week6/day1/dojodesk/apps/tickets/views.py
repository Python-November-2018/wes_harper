from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Ticket
from ..users.models import User

# Create your views here.
def index(req):
  if 'user_id' not in req.session:
    return redirect('users:new')

  context = {
    'all_tickets': Ticket.objects.all()
  }
  return render(req, 'tickets/index.html', context)

def new(req):
  if 'user_id' not in req.session:
    return redirect('users:new')
  context = {
    "assignees": User.objects.all()
  }
  return render(req, 'tickets/new.html', context)

def create(req):
  errors = Ticket.objects.validate(req.POST)
  if errors:
    for error in errors:
      messages.error(req, error)
    return redirect('tickets:new')

  Ticket.objects.create_ticket(req.POST)
  return redirect('tickets:index')

def show(req, id):
  context = {
    'ticket': Ticket.objects.get(id=id)
  }
  return render(req, 'tickets/show.html', context)