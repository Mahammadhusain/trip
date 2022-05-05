from django.db import models
from django.contrib.auth.models import User

vehical_type = [['Car','Car'],['Bus','Bus'],['Train','Train'],['Flight','Flight']]

class VehicleModel(models.Model):
    provider = models.CharField(max_length=200)
    from_location = models.CharField(max_length=200)
    to_location = models.CharField(max_length=200)
    price = models.IntegerField()
    duration = models.CharField(max_length=200)
    v_class = models.CharField(max_length=200)
    v_type = models.CharField(choices=vehical_type,max_length=100)

    objects= models.Manager()


class BookingModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    fname = models.CharField(max_length=300)
    lname = models.CharField(max_length=300)
    mobile = models.IntegerField()
    email = models.EmailField(max_length=300)
    gender = models.CharField(max_length=100)
    provider = models.CharField(max_length=100)
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    class_type = models.CharField(max_length=100)
    v_type = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    book_date = models.DateTimeField(auto_now_add=True)
    gst = models.IntegerField(default=0)
    total = models.IntegerField()
    

    objects = models.Manager()

    def __str__(self):
        return self.fname


    