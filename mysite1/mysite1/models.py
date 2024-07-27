from django.db import models


class Main_Page_Website(models.Model):
    objects = None
    Name = models.CharField(max_length=50)
    Occupation = models.CharField(max_length=100)
    Email = models.EmailField()

    class Meta:
        app_label = 'mysite1'