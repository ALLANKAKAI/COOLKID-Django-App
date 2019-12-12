from django.db import models
from django.contrib.postgres.fields import JSONField
# Create your models here.

COUNTY = (
    ('bungoma','Bungoma'),
    ('busia','Busia'),
    ('kakamega','Kakamega'),
    ('kisumu','Kisumu'),
    ('mombasa','Mombasa'),
    ('nairobi','Nairobi'),
    ('nakuru','Nakuru')
)

GENDER = (
    ('male','Male'),
    ('female','Female'),
    ('other','Other')
)

class Contestant(models.Model):
    full_name = models.CharField(max_length=200)
    ig_username = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=12)
    county = models.CharField(max_length=50,choices=COUNTY)
    gender = models.CharField(max_length=20,choices=GENDER)
    image = models.ImageField(upload_to='images')
    approved = models.BooleanField(default=False)
    def __str__(self):
        return self.full_name
