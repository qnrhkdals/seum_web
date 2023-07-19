from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=50)
    ans_url = models.CharField(max_length=255)
    min_num = models.IntegerField()
    max_num = models.IntegerField()

    def __str__(self):
        return self.name
    
class Deadline(models.Model):
    date = models.CharField(max_length=30)

    def __str__(self):
        return self.date