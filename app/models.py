# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=50)
    image_link = models.CharField(max_length=200, default="/static/assets/img/default.jpg")
    cat_margin = models.DecimalField(max_digits=20,decimal_places=2, default=0.00);

    def get_absolute_url(self):
        return f"/category/{self.id}/"

class Invoice(models.Model):
    supplier = models.CharField(max_length=50)
    invoice_nr = models.IntegerField()
    date = models.DateField()
    products = models.CharField(max_length=2000, default="", null=True, blank=True) #standard format: "[Product_id1,Amount1];[...]"
    totalin = models.DecimalField(max_digits=20,decimal_places=2, default=0.00, null=True, blank=True);
    totalout = models.DecimalField(max_digits=20,decimal_places=2, default=0.00, null=True, blank=True);
    totalmargin = models.DecimalField(max_digits=20, decimal_places=2, default=0.00, null=True, blank=True);

    def get_absolute_url(self):
        return f"/invoice/{self.id}/"

class Supplier(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/supplier/{self.id}/"