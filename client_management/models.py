# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=15, null=False)
    last_name = models.CharField(max_length=35, null=False)
    iban = models.CharField(max_length=24, null=False)
    created_by = models.EmailField()

    class Meta:
        db_table = "client"

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name, self.iban)