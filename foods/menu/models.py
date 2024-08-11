from django.db import models

# Create your models here.
class dinner(models.Model):
    name=models.CharField(max_length=20)
    price=models.IntegerField()
    category=models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class notePad(models.Model):
    title=models.CharField(max_length=20)
    content=models.TextField()

    def __str__(self):
        return self.title
    
