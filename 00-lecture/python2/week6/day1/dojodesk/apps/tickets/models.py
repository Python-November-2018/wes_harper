from django.db import models
from ..users.models import User

# Create your models here.
class TicketManager(models.Manager):
  def validate(self, form_data):
    errors = []

    if len(form_data['title']) < 3:
      errors.append("Title must be at least 3 characters long")
    if len(form_data['description']) < 3:
      errors.append("Description must be at least 3 characters long")

    try:
      priority = int(form_data['priority'])
      if priority > 5 or priority < 1:
        errors.append("Priority must be between 1 and 5")
    except:
      errors.append("Priority must be a number")

    valid_statuses = ["New", "In Progress", "Done"]
    if form_data['status'] not in valid_statuses:
      errors.append("Invalid status")

    try:
      User.objects.get(id=form_data['assignee'])
    except:
      errors.append("Invalid assignee")

    return errors

  def create_ticket(self, form_data):
    # get user
    # doesn't need try/catch due to validations from self.validate
    assignee = User.objects.get(id=form_data['assignee'])
    self.create(
      title = form_data['title'],
      description = form_data['description'],
      status = form_data['status'],
      # this is also handled in validations
      priority = int(form_data['priority']),
      assignee = assignee,
    )

  def update_ticket(self, form_data, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    assignee = User.objects.get(id=form_data['assignee'])

    ticket.title = form_data['title']
    ticket.description = form_data['description']
    ticket.priority = int(form_data['priority'])
    ticket.status = form_data['status']
    ticket.assignee = assignee
    ticket.save()
  
  def delete_ticket(self, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.delete()

class Ticket(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  status = models.CharField(max_length=255)
  priority = models.IntegerField()
  assignee = models.ForeignKey(User, related_name="tickets")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = TicketManager()