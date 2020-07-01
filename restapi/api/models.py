from django.db import models

class apiModel(models.Model):
    name = models.CharField(max_length = 10)
    phone = models.IntegerField()
    email = models.EmailField()