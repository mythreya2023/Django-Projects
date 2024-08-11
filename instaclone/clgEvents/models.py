from django.db import models


# Create your models here.

class Event(models.Model):
    eveName = models.CharField(max_length=40)
    eveDesc = models.TextField()
    eveDate = models.DateField()
    eveImg = models.ImageField(upload_to='media',null=True)
    eveBranch = models.CharField(max_length=10)
    eveYear = models.IntegerField()

    def __str__(self):
        return self.eveName
    

class RegEvent(models.Model):
    event = models.ForeignKey("Event",on_delete=models.CASCADE)
    user = models.ForeignKey("auth.User",on_delete=models.CASCADE)

    def __str__(self):
        return self.event.eveName
