# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError

from .models import Post
from .forms import ContactsForm


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def main(request):
    posts = Post.objects.filter(interesting=True)[:5]
    return render(request, 'blog/main.html', {'posts': reversed(posts)})


def contacts(request):
    if request.method == 'POST':
        form = ContactsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = 'Вам пришло новое сообщение с сайта Fresh News! \n\nОтправитель: ' + name + '\nEmail Адрес: ' \
                      + email + '\nСообщение: ' + form.cleaned_data['message']
            recipients = ['hazardous333@mail.ru', 'serhei1994@yandex.ru']
            theme = 'Новое сообщение с сайта Fresh News!'

            try:
                send_mail(theme, message, 'tkachev9457@gmail.com', recipients)
            except BadHeaderError:  # Защита от уязвимости
                return HttpResponse('Invalid header found')
    return render(request, 'blog/contacts.html')
