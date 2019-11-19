from django.shortcuts import render
from django.utils import timezone
from .models import Post
def post_list(request):
    return render(request, 'blog/post_list.html', {})
def inna(request):
    return render(request, 'blog/inna.html')
