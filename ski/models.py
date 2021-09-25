from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    is_Client = models.BooleanField(default=False)


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    zipcode = models.CharField(max_length=50, blank=True)
    phone = models.CharField(blank=True, max_length=20)

    def __str__(self):
        return self.user.username


class Product(models.Model):
    product_name = models.CharField(max_length=200, blank=False)
    product_description = models.CharField(max_length=2500, blank=False)
    product_image = models.ImageField(upload_to='Static', blank=True)

    def __str__(self):
        return self.product_name


class Request(models.Model):
    request_description = models.CharField(max_length=2500, blank=False)
    request_start_date = models.DateField
    request_return_date = models.DateField
    order_status = (
        ('y', 'approved'),
        ('n', 'declined'),
    )
    request_order_status = models.CharField(max_length=1, choices=order_status)

    def __str__(self):
        return self.request_start_date
