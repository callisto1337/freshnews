# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post
from .forms import ContactsForm


# def events(request):
#     posts = Post.objects.filter(published=True, category=2).order_by('-date_created')
#     return render(request, 'blog/events.html', {'posts': posts})
#
#
# def telekom(request):
#     posts = Post.objects.filter(published=True, category=1).order_by('-date_created')
#     return render(request, 'blog/telekom.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.category == 1:
        post.category_id = 1
    elif post.category == 2:
        post.category_id = 2
    elif post.category == 3:
        post.category_id = 3
    return render(request, 'blog/post_detail.html', {'post': post})


def main(request):
    post_list = Post.objects.filter(published=True).order_by('-date_created')
    paginator = Paginator(post_list, 5)

    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/main.html', {'posts': posts})


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
