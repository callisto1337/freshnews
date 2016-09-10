# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError

from .models import Post
from .forms import ContactsForm


def main(request):
    posts = Post.objects.filter(interesting=True)[:5]
    return render(request, 'blog/main.html', {'posts': posts})


def contacts(request):
    if request.method == 'POST':
        form = ContactsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = 'Вам пришло новое сообщение с сайта Fresh News! \n\nОтправитель: ' + name + '\nEmail Адрес: ' \
                      + email + '\nСообщение: ' + form.cleaned_data['message']
            recipients = ['hazardous333@mail.ru']
            theme = 'Новое сообщение с сайта Fresh News!'

            try:
                send_mail(theme, message, 'hazardous333@gmail.com', recipients)
            except BadHeaderError:  # Защита от уязвимости
                return HttpResponse('Invalid header found')
            return render(request, 'blog/contacts.html')
    else:
        return render(request, 'blog/contacts.html')
