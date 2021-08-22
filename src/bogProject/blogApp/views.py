from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from .models import BlogPost, Category, Tags

# Create your views here.

# def home(request):
#     return render(request, 'blogApp/home.html')

class BlogPostCreateView(LoginRequiredMixin, CreateView):
   model = BlogPost
   template_name = 'blogApp/post.html'
   fields = ['title', 'article', 'prictue', 'category', 'tags']
   # exclude = ('author', 'created_at',)
   def form_valid(self, form):
      form.instance.author = self.request.user
      return super().form_valid(form)




class BlogPostUpdateView(LoginRequiredMixin, UpdateView):
   model = BlogPost
   template_name = 'blogApp/post_update.html'
   fields = ['title', 'article', 'prictue', 'category', 'tags']
   # exclude = ('author', 'created_at',)
   def form_valid(self, form):
      form.instance.author = self.request.user
      return super().form_valid(form)



class BlogPostListView(ListView):
   model = BlogPost
   template_name = 'blogApp/home.html'
   context_object_name = 'blog'


   def get_queryset(self):
      queryset = BlogPost.objects.filter(self.author=='admin')
      return queryset







class BlogPostDetailView(DetailView):
   model = BlogPost
   template_name = 'blogApp/blogDetail.html'
   context_object_name = 'blog'

   def get_context_data(self, **kwargs):
      data = super().get_context_data(**kwargs)
      data['c'] = Category.objects.all()
      return data

# b = BlogPost.objects.all(author=request.user)