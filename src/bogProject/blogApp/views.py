from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DeleteView
from django.views.generic.detail import DetailView
from .models import BlogPost, Category, Tags
# Create your views here.

# def home(request):
#     return render(request, 'blogApp/home.html')

class BlogPostListView(ListView):
   model = BlogPost
   template_name = 'blogApp/home.html'
   context_object_name = 'blog'




class BlogPostDetailView(DetailView):
   model = BlogPost
   template_name = 'blogApp/blogDetail.html'
   context_object_name = 'blog'