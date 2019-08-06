# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from client_management.models import Client
from client_management.forms import ClientForm


def main(request):
    clients = Client.objects.all()
    return render(request, "main.html", {'clients': clients})


def add(request):
    return render(request, 'add.html')


def create(request):
    form = ClientForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("/main")
    return render(request, 'add.html')
