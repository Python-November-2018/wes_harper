from django.db import models
from ..tickets.models import Ticket
from ..users.models import User

# Create your models here.
class Comment(models.Model):
  content = models.TextField()
  ticket = models.ForeignKey(Ticket, related_name="comments")
  user = models.ForeignKey(User, related_name="comments")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)