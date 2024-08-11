from django.db import models

# Create your models here.
class post(models.Model):
    uname=models.CharField(max_length=30)
    content=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.uname