from django.db import models

# Create your models here.
class User(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  username = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  pw_hash = models.CharField(max_length=500)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.email