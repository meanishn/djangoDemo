from django.shortcuts import render
from demo.models import Post
# Create your views here.

def index(request):
    post_list = Post.objects.all()
    return render(request, "demo/index.html", {'posts':post_list})
    