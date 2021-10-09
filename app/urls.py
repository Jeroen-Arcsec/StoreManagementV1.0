# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views

urlpatterns = [

    # The home page
    path('', views.overview, name='home'),
    path('tables', views.new_invoice, name='new_invoice'),
    path('create', views.invoice_create_view, name='create'),

    #Categories
    path('categories', views.category_list_view, name='categories'),
    path('create_category', views.category_creation, name='create_categories'),
    path('category/<int:pk>/', views.category_edit, name='create_views'),

    #Suppliers
    path('suppliers', views.supplier_list_view, name='suppliers'),
    path('create_supplier', views.supplier_creation, name='create_supplier'),

    #Invoices
    path('invoices', views.invoice_list_view, name='invoices'),
    path('create_invoice', views.invoice_creation, name='create_invoices'),
    path('invoice/<int:pk>/', views.invoice_edit, name='create_views'),

    #change content based on the category chosen
    #passes id to the dynamic lookup view
    path('create/<int:pk>/', views.dynamic_lookup_view, name='create_views'),
    path('list', views.product_list_view, name='create'),

    #Overview
    path('overview', views.overview, name='overview'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
