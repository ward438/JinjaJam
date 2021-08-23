import datetime
from django.db import models
from django.utils import timezone

class Address(models.Model):
    city = models.CharField(max_length=200)  
    state = models.CharField(max_length=200)  
    zip = models.CharField(max_length=5)  

    def __str__(self):
        return f"{self.city}, {self.state} - {self.zip}"

class Person(models.Model):

    name_first = models.CharField(max_length=200)
    name_last = models.CharField(max_length=200)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True) 
    
    def __str__(self):
        return f"{self.name_first}, {self.name_last}"
        # (self.name_first + self.name_last)# + self.address)
        # return (self.name_first)



    