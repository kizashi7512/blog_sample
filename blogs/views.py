from django.shortcuts import render
from .models import Blog

def index(request):
    blogs = Blog.objects.order_by('-created_datetime')
    return render(request, 'blogs/index.html', {'blogs': blogs})
    #メモ
    #renderメソットはrequest情報を元にしてindex.htmlを表示すること

def detail(request, blog_id):
  blog = Blog.objects.get(id=blog_id)
  return render(request, 'blogs/detail.html', {'blog': blog})
