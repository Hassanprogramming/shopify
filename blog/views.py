from django.shortcuts import render
from .models import *
# Create your views here.
def News(request):
    admin = Admin.objects.all()
    news = New.objects.all()
    blogs = Blogs.objects.all()
    context = {'blogs': blogs, 'news':news, 'admin':admin}
    return render(request, "blog/News.html", context)