from django.contrib import admin
from .models import*
# Register your models here.

admin.site.register(User)
admin.site.register(Client)
admin.site.register(Employee)
admin.site.register(Product)
admin.site.register(Request)