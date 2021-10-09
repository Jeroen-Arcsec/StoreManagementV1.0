# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import ast

import simplejson
from click import edit
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django import template
from django.urls import reverse
from .models import Category
from .models import Supplier
from .models import Invoice
from .forms import CreateInvoiceForm, CreateCategoryForm, CreateSupplierForm
import json
import datetime


@login_required(login_url="/login/")
def index(request):
    context = {}
    context['segment'] = 'index'
    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def new_invoice(request):
    print("testing_routing")
    obj = Category.objects.all()
    print(obj[0].name)
    Supplier
    context = {"categories": obj}

    # invoice_instance = get_object_or_404(BookInstance, pk=pk)

    # If this is a POST request then process the Form data
    # if request.method == 'POST':

    # Create a form instance and populate it with data from the request (binding):
    # form = RenewBookForm(request.POST)

    # Check if the form is valid:
    # if form.is_valid():
    # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
    #   invoice_instance.due_back = form.cleaned_data['renewal_date']
    #   invoice_instance.save()

    # redirect to a new URL:
    # return HttpResponseRedirect(reverse('all-borrowed') )

    # If this is a GET (or any other method) create the default form.
    # else:
    #   proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
    #  form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

    # context = {
    #  'form': form,
    #   'book_instance': invoice_instance,
    # }

    html_template = loader.get_template('create_invoice.html')
    return HttpResponse(html_template.render(context, request))

def invoice_create_view2(request):
    form = CreateInvoiceForm(request.POST or None)
    if form.is_valid():
        form.save()
    print(request.POST)
    newtitle = request.POST.get('title')
    #Product.objects.create(title=newtitle)
    obj = Category.objects.all()

    html_template = loader.get_template('test.html')
    context={
        #'form':form,
        "categories": obj,
    }
    return HttpResponse(html_template.render(context, request));

def invoice_create_view(request):
    data = {
        'supplier': "Colruyt"
    }
    obj = Supplier.objects.get(id=1)
    cat_form = RawCategoryForm()
    if request.method == "POST":
        cat_form = RawCategoryForm(request.POST or None,initial=data, instance=obj) #one of the two, the second really changes the object specified
        if cat_form.is_valid():
            print(cat_form.cleaned_data)
            Category.objects.create(**cat_form.cleaned_data)
        else:
            print(cat_form.errors)
    context={"form":cat_form}

    html_template = loader.get_template('test.html')
    return HttpResponse(html_template.render(context, request));

def dynamic_lookup_view(request, pk):
    #obj = Category.objects.get(id=pk)
    obj = get_object_or_404(Category, id=pk)
    #Only on POST request
    if request.method =="POST":
        obj.delete()
        return redirect('/')
    context={
        "object": obj
    }

    html_template = loader.get_template('test.html')
    return HttpResponse(html_template.render(context, request));

def product_list_view(request):
    queryset = Category.objects.all()
    context={
        "objectlist": queryset
    }
    html_template = loader.get_template('test.html')
    return HttpResponse(html_template.render(context, request));

def category_list_view(request):
    queryset = Category.objects.all()
    context={
        "categories": queryset
    }
    html_template = loader.get_template('Categories.html')
    return HttpResponse(html_template.render(context, request));

def category_creation(request):

    cat_form = CreateCategoryForm()
    html_template = loader.get_template('create_category.html')
    if request.method == "POST":
        cat_form = CreateCategoryForm(request.POST or None) #one of the two, the second really changes the object specified
        if cat_form.is_valid():
            Category.objects.create(**cat_form.cleaned_data)
            return HttpResponseRedirect('/categories')
        else:
            print(cat_form.errors)

    context={"form":cat_form}
    return HttpResponse(html_template.render(context, request));

def category_edit(request, pk):
    category = Category.objects.get(id=pk)

    cat_form = CreateCategoryForm(initial={'name': category.name, 'image_link': category.image_link, 'cat_margin':category.cat_margin})
    html_template = loader.get_template('edit_category.html')
    if request.method == "POST":
        cat_form = CreateCategoryForm(request.POST or None) #one of the two, the second really changes the object specified
        if cat_form.is_valid():
            Category.objects.create(**cat_form.cleaned_data)
            Category.objects.get(id=pk).delete()
            return HttpResponseRedirect('/categories')
        else:
            print(cat_form.errors)

    context={"form":cat_form}
    return HttpResponse(html_template.render(context, request));

def supplier_list_view(request):
    queryset = Supplier.objects.all()
    print(queryset)
    context={
        "suppliers": queryset
    }
    html_template = loader.get_template('suppliers.html')
    return HttpResponse(html_template.render(context, request));

def supplier_creation(request):
    cat_form = CreateSupplierForm()
    html_template = loader.get_template('create_supplier.html')
    if request.method == "POST":
        cat_form = CreateSupplierForm(request.POST or None) #one of the two, the second really changes the object specified
        if cat_form.is_valid():
            Supplier.objects.create(**cat_form.cleaned_data)
            return HttpResponseRedirect('/suppliers')
        else:
            print(cat_form.errors)

    context={"form":cat_form}
    return HttpResponse(html_template.render(context, request));

def invoice_list_view(request):
    queryset = Invoice.objects.all()
    print(queryset)
    context={
        "invoices": queryset
    }
    html_template = loader.get_template('invoices.html')
    return HttpResponse(html_template.render(context, request));

def format_products(names, links, buyvals, sellvals, margins):
    string = ""
    for i in range(len(names)-1):
        string = "["+str(names)+","+str(links)+","+str(buyvals)+","+str(sellvals)+","+str(margins)+"]"
    return string

def invoice_creation(request):
    invoice_form = CreateInvoiceForm()
    html_template = loader.get_template('create_invoice.html')
    suppliers = Supplier.objects.all()
    categories = Category.objects.all()

    data = []
    for category in categories:
        data.append({'name': category.name, 'link': category.image_link, 'margin': category.cat_margin})
    category_data = simplejson.dumps(data)

    if request.method == "POST":
        requested = request.POST
        print(requested)

        invoice_nr = requested.get("invoice_nr")
        supplier = requested.get("supplier")
        date = requested.get("date")

        names = requested.getlist("names")
        buyvals = requested.getlist("buyvalues")
        sellvals = requested.getlist("sellvalues")
        margins = requested.getlist("marginvalues")
        links = requested.getlist("links")

        totalin = buyvals[-1]
        totalout = sellvals[-1]
        totalmargin = margins[-1]
        print(names)
        products = format_products(names, links, buyvals, sellvals, margins)
        print(products)

        invoice_form = CreateInvoiceForm(request.POST or None) #one of the two, the second really changes the object specified
        if invoice_form.is_valid():
            print(invoice_form.cleaned_data['supplier'])
            invoice_form.cleaned_data['products'] = products
            invoice_form.cleaned_data['totalin'] = totalin
            invoice_form.cleaned_data['totalout'] = totalout
            invoice_form.cleaned_data['totalmargin'] = totalmargin
            Invoice.objects.create(**invoice_form.cleaned_data)
            return HttpResponseRedirect('/invoices')
        else:
            print(invoice_form.errors)

    context = {"form": invoice_form, "suppliers": suppliers, "categories": categories, "category_data": category_data}

    return HttpResponse(html_template.render(context, request));

def invoice_edit(request, pk):
    edit_invoice = Invoice.objects.get(id=pk)
    edit_invoice_nr = edit_invoice.invoice_nr
    edit_supplier = edit_invoice.supplier
    edit_date = edit_invoice.date

    edit_products = ast.literal_eval(edit_invoice.products)

    names = edit_products[0]
    links = edit_products[1]
    buy = list(map(float,edit_products[2]))
    sell = list(map(float,edit_products[3]))
    margin = list(map(float,edit_products[4]))

    invoice_form = CreateInvoiceForm(initial={'supplier': edit_supplier, 'invoice_nr': edit_invoice_nr, 'date':edit_date})
    html_template = loader.get_template('edit_invoice.html')
    suppliers = Supplier.objects.all()
    categories = Category.objects.all()
    data = []
    for category in categories:
        data.append({'name': category.name, 'link': category.image_link, 'margin': category.cat_margin})
    category_data = simplejson.dumps(data)

    if request.method == "POST":
        requested = request.POST
        print(requested)

        invoice_nr = requested.get("invoice_nr")
        supplier = requested.get("supplier")
        date = requested.get("date")

        names = requested.getlist("names")
        buyvals = requested.getlist("buyvalues")
        sellvals = requested.getlist("sellvalues")
        margins = requested.getlist("marginvalues")
        links = requested.getlist("links")

        totalin = buyvals[-1]
        totalout = sellvals[-1]
        totalmargin = margins[-1]
        products = format_products(names, links, buyvals, sellvals, margins)

        invoice_form = CreateInvoiceForm(request.POST or None) #one of the two, the second really changes the object specified
        if invoice_form.is_valid():
            print(invoice_form.cleaned_data['supplier'])
            invoice_form.cleaned_data['products'] = products
            invoice_form.cleaned_data['totalin'] = totalin
            invoice_form.cleaned_data['totalout'] = totalout
            invoice_form.cleaned_data['totalmargin'] = totalmargin
            Invoice.objects.create(**invoice_form.cleaned_data)
            Invoice.objects.get(id=pk).delete()
            return HttpResponseRedirect('/invoices')
        else:
            print(invoice_form.errors)

    context = {"form": invoice_form, "suppliers": suppliers, "categories": categories, "category_data": category_data, "names":names, "links":links, "buy":buy, "sell":sell, "margin":margin }

    return HttpResponse(html_template.render(context, request));

def date_formatted_data(invoices, suppliers, categories, daterange):
    overviews = []
    for key in daterange:
        print(key)
        before = daterange[key][0]
        after = daterange[key][1]
        overview = {}
        overview[key] = list(daterange.keys())[0]
        for supplier in suppliers:
            overview[supplier.name] = {}
            for category in categories:
                overview[supplier.name][category.name] = [category.name,category.image_link,float(category.cat_margin),0, 0]  # buy, sell
                overview[supplier.name]["TOTAAL"] = ["TOTAAL", "/static/assets/img/total.png" ,0.00 ,0, 0]  # buy, sell

        for invoice in invoices:
            if  before <= invoice.date <= after:
                array = ast.literal_eval(invoice.products)
                cats = array[0]
                links = array[1]
                buyval = list(map(float, list(array[2])))
                sellval = list(map(float, list(array[3])))
                marginval = array[4]
                for i in range(len(cats)):
                    overview[invoice.supplier][cats[i]][3] = overview[invoice.supplier][cats[i]][3] + buyval[i]
                    overview[invoice.supplier][cats[i]][4] = overview[invoice.supplier][cats[i]][4] + sellval[i]
                overviews.append(overview)
    return overviews


def daterange_format(start_date, end_date):
    start_year = start_date.year
    end_year = end_date.year
    quarters = {}
    for i in range(0,end_year-start_year+1):
        print(i)
        quarters["1ste " + str(start_year+i)] = [datetime.date(start_year+i, 1, 1), datetime.date(start_year+i, 3,31)]  # start and end dates for quarters
        quarters["2de " + str(start_year+i)] = [datetime.date(start_year+i, 4, 1), datetime.date(start_year+i, 6,30)]  # start and end dates for quarters
        quarters["3de " + str(start_year+i)] = [datetime.date(start_year+i, 7, 1), datetime.date(start_year+i, 9,30)]  # start and end dates for quarters
        quarters["4de " + str(start_year+i)] = [datetime.date(start_year+i, 10, 1), datetime.date(start_year+i, 12,31)]  # start and end dates for quarters
    return quarters

def overview(request):
    invoices = Invoice.objects.all()
    suppliers = Supplier.objects.all()
    categories = Category.objects.all()

    start_date = datetime.date.today()
    for invoice in invoices:
        if(invoice.date <= start_date):
            start_date = invoice.date

    end_date =  datetime.date.today()
    delta = datetime.timedelta(days=1)

    daterange = daterange_format(start_date, end_date)
    data = date_formatted_data(invoices,suppliers,categories,daterange)
    suppliersarray = [suppliers[i].name for i in range(len(suppliers))]
    print(suppliersarray)

    context = {"data": data, "suppliers": suppliersarray}
    html_template = loader.get_template('overview.html')
    return HttpResponse(html_template.render(context, request));