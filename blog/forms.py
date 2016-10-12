# -*- coding: utf-8 -*-
from django import forms


class ContactsForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()