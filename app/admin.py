# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

# Register your models here.
from .models import Supplier
from .models import Category
from .models import Invoice

admin.site.register(Supplier)