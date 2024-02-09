from django.db import models

# Create your models here.


class Notite(models.Model):
    id_notita = models.IntegerField(primary_key=1)
    text_notita = models.CharField(max_length=500)

