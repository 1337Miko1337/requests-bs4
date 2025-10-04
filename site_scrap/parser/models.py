from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=255)
    color = models.JSONField(null=True, blank=True)
    memory = models.JSONField(null=True, blank=True)
    price = models.CharField(max_length=255)
    photo = models.JSONField(null=True, blank=True)
    code = models.CharField(max_length=255)
    fb = models.CharField(max_length=255)
    characteristics = models.JSONField(null=True, blank=True)
