# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from datetime import datetime
from email.mime import image

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from .models import Supplier
from .models import Invoice
from .models import Category
import datetime

class CreateCategoryForm(forms.ModelForm):
    name = forms.CharField()
    cat_margin = forms.DecimalField(initial=0.00, decimal_places=2)
    image_link = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control border-1 ps-3'
            })

    class Meta:
        model = Category
        fields = [
            'name',
            'image_link',
            'cat_margin'
        ]

    def clean_cat_margin(self,*args,**kwargs):
        cat_margin = self.cleaned_data.get("cat_margin")
        if not (0 <= cat_margin <= 100):
            raise forms.ValidationError("De marge moet tussen 0 en 100% bedragen.")
        else:
            return cat_margin

    def clean_image_link(self,*args,**kwargs):
        image_link = self.cleaned_data.get("image_link")
        if image_link == "":
            return "/static/assets/img/default.jpg"
        else:
            return image_link

class CreateSupplierForm(forms.ModelForm):
    name = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control border-1 ps-3'
            })

    class Meta:
        model = Category
        fields = [
            'name'
        ]

class DateInput(forms.DateInput):
    input_type = 'date'

class CreateInvoiceForm(forms.ModelForm):
    supplier = forms.ModelChoiceField(queryset=Supplier.objects.all(), to_field_name='name')
    invoice_nr = models.IntegerField()
    date = models.DateField(default=datetime.date.today())
    products = models.CharField(blank=False) #standard format: "[cat_id1,Amount1];[...]"
    totalin = models.DecimalField(decimal_places=2);
    totalout = models.DecimalField(decimal_places=2);
    totalmargin = models.DecimalField(decimal_places=2);


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['supplier'].required = False
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control border-1 ps-3'
            })

    class Meta:
        model = Invoice
        fields = [
            'supplier',
            'invoice_nr',
            'date',
            'products',
            'totalin',
            'totalout',
            'totalmargin'
        ]
        widgets = {
            'date': DateInput(format=('%Y-%m-%d')),
        }