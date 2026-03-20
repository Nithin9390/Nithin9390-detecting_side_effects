from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=3000)
    gender = models.CharField(max_length=300)

class detect_drug_reactions(models.Model):

    Fid= models.CharField(max_length=3000)
    Drug_Name1= models.CharField(max_length=3000)
    Reason1= models.CharField(max_length=3000)
    Drug_Name2= models.CharField(max_length=3000)
    Reason2= models.CharField(max_length=3000)
    Rating= models.CharField(max_length=3000)
    Reviews= models.CharField(max_length=3000)
    Drugfollowers= models.CharField(max_length=3000)
    Prediction= models.CharField(max_length=3000)

class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



