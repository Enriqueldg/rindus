from django import forms

from client_management.models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"
