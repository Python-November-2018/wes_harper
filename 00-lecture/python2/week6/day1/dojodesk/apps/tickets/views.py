from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Ticket
from ..users.models import User
from django.core import serializers
import json

# Create your views here.
def index(req):
  if 'user_id' not in req.session:
    return redirect('users:new')

  context = {
    'user_tickets': Ticket.objects.filter(assignee=req.session['user_id']),
    'other_tickets': Ticket.objects.exclude(assignee=req.session['user_id']),
    'user_info': User.objects.get(id=req.session['user_id'])
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
  if 'user_id' not in req.session:
    return redirect('users:new')

  if req.method != 'POST':
    return redirect('tickets:new')

  errors = Ticket.objects.validate(req.POST)
  if errors:
    for error in errors:
      messages.error(req, error)
    return redirect('tickets:new')

  Ticket.objects.create_ticket(req.POST)
  return redirect('tickets:index')

def show(req, ticket_id):
  if 'user_id' not in req.session:
    return redirect('users:new')

  try:
    context = {
      'ticket': Ticket.objects.get(id=ticket_id),
    }
  except:
    return redirect('tickets:index')

  return render(req, 'tickets/show.html', context)

def edit(req, ticket_id):
  if 'user_id' not in req.session:
    return redirect('users:new')

  try:
    context = {
      'ticket': Ticket.objects.get(id=ticket_id),
      'priority_list': [1, 2, 3, 4, 5],
      'status_list': ["New", "In Progress", "Done"],
      'assignees': User.objects.all()
    }
  except:
    return redirect('tickets:index')

  return render(req, 'tickets/edit.html', context)

def update(req, ticket_id):
  if 'user_id' not in req.session:
    return redirect('users:new')
  if req.method != 'POST':
    return redirect('tickets:edit', ticket_id)

  errors = Ticket.objects.validate(req.POST)
  if errors:
    for error in errors:
      messages.error(req, error)
    return redirect('tickets:edit', ticket_id)
  
  Ticket.objects.update_ticket(req.POST, ticket_id)
  return redirect('tickets:index')

def delete(req, ticket_id):
  Ticket.objects.delete_ticket(ticket_id)
  return redirect('tickets:index')

def ajax_new(req):
  if 'user_id' not in req.session:
    return redirect('users:new')

  context = {
    "assignees": User.objects.all()
  }
  return render(req, 'tickets/ajax-new.html', context)

def ajax_create(req):
  errors = Ticket.objects.validate(req.POST)
  if errors:
    return HttpResponse(json.dumps(errors), content_type='application/json', status=400)

  ticket = Ticket.objects.create_ticket(req.POST)
  return HttpResponse(serializers.serialize('json', [ticket]), content_type='application/json', status=200)