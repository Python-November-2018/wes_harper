from django.db import models
from ..tickets.models import Ticket
from ..users.models import User

# Create your models here.
class CommentManager(models.Manager):
  def validate(self, form_data, user_id):
    errors = []
    try:
      User.objects.get(id=user_id)
    except:
      errors.append("User not found")

    try:
      Ticket.objects.get(id=form_data['ticket'])
    except:
      errors.append("Ticket not found")
    
    if len(form_data['content']) < 5:
      errors.append("Comment must be at least 5 characters")
    
    return errors

  def create_comment(self, form_data, user_id):
    user = User.objects.get(id=user_id)
    ticket = Ticket.objects.get(id=form_data['ticket'])
    self.create(
      content = form_data['content'],
      user = user,
      ticket = ticket,
    )

class Comment(models.Model):
  content = models.TextField()
  ticket = models.ForeignKey(Ticket, related_name="comments")
  user = models.ForeignKey(User, related_name="comments")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = CommentManager()