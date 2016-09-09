from django.shortcuts import render
from .models import Post

def main(request):
    posts = Post.objects.filter(interesting=True)[:5]
    return render(request, 'blog/main.html', {'posts': posts})

def contacts(request):
    return render(request, 'blog/contacts.html')
