from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.user)
admin.site.register(models.Student)
admin.site.register(models.Cont)
# admin.site.register(models.otp_verification)