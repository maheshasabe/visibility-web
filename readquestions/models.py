from django.db import models

# Create your models here.

class Platforms(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='readquestions/images')
    url = models.URLField(blank=True)
    company = models.CharField(max_length=200) 
    description = models.TextField()
    onboardDate = models.DateField()

    def __str__(self):
        return self.name