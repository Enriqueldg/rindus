# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404

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


def edit(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    return render(request, 'edit.html', {'client': client})


def update(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    form = ClientForm(request.POST, instance=client)
    if form.is_valid():
        form.save()
        return redirect("/main")
    return render(request, 'edit.html', {'client': client})
