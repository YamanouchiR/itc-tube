from django.shortcuts import render
from random import randint
from .models import NippoModel
from .forms import NippoFormClass

def nippoListView(request):
    template_name = "nippo/nippo-list.html"
    ctx = {}
    qs = NippoModel.objects.all()
    ctx["object_list"] = qs
    return render(request, template_name, ctx)

def nippoDetailView_old(request,number):
    template_name="nippo/nippo-detail.html"
    random_int = randint(1,10)
    ctx = {
        "random_number": random_int,
        "number":number
    }
    return render(request, template_name, ctx)

def nippoDetailView(request, pk):
    template_name = "nippo/nippo-detail.html"
    ctx = {}
    q = NippoModel.objects.get(pk=pk)
    ctx["object"] = q
    return render(request, template_name, ctx)

def nippoCreateView(request):
    template_name="nippo/nippo-form.html"
    form = NippoFormClass()
    ctx = {}
    ctx["form"] = form
    return render(request, template_name, ctx)