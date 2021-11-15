from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

# Create your models here.


class User(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=200,blank=True, null=True)
    city = models.CharField(max_length=50,blank=True, null=True)
    state = models.CharField(max_length=50,blank=True, null=True)
    zipcode = models.CharField(max_length=10,blank=True, null=True)
    phone = models.CharField(max_length=50,blank=True, null=True)

    def __str__(self):
        return self.user.username


class Product(models.Model):
    product_name = models.CharField(max_length=200, blank=False)
    product_description = models.TextField(blank=True)
    product_image = models.ImageField(upload_to='Static', blank=True)

    def __str__(self):
        return self.product_name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    order_date = models.DateField(default=timezone.now, null=True)
    order_start_date=models.DateField(blank=True, null=True)
    order_return_date = models.DateField(blank=True, null=True)
    order_options = (
        ('pending', 'PENDING'),
        ('approved', 'APPROVED'),
        ('declined', 'DECLINED'),
    )
    order_status = models.CharField(max_length=30, choices=order_options,null=False, default='Pending')
