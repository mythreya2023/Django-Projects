from django.db import models

# Create your models here.

class notify(models.Model):
    data=models.CharField(max_length=20)

    def __str__(self):
        return self.data
    
