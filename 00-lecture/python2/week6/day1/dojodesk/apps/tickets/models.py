from django.db import models
from ..users.models import User

# Create your models here.
class Ticket(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  status = models.CharField(max_length=255)
  priority = models.IntegerField()
  assignee = models.ForeignKey(User, related_name="tickets")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)