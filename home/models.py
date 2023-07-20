from django.db import models

# Create your models here.


class staffs(models.Model):
    staff_name=models.CharField(max_length=100)
    staff_description=models.TextField()

    def __str__(self):
        return self.staff_name

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class booking(models.Model):
    p_name=models.CharField(max_length=100)
    p_phone=models.CharField(max_length=100)
    p_email=models.EmailField()
    doc_name=models.ForeignKey('Doctor',on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)