from django.shortcuts import render
from .models import Post

# Create your views here.
def list_post(request):
    posts = Post.objects.all().order_by('-creation_date')
    return render(request, 'blog/list_post.html', {'posts': posts})

# def list_post(request):
#     return render(request, 'blog/list_post.html', context={
#         'title' : ''
#     })