# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from client_management.models import Client


def main(request):
    clients = Client.objects.all()
    return render(request, "main.html", {'clients': clients})
