from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    

class Accommodation(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)



class DestinationDetails(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    accommodations = models.ManyToManyField(Accommodation)
   
   

class TravelOptions(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)




