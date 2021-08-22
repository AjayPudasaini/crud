from os import name
from django.urls import path
from . import views

urlpatterns = [
   # path('', views.home, name='home'),
   path('', views.BlogPostListView.as_view(), name='home'),
   path('detail/<int:pk>', views.BlogPostDetailView.as_view(), name='detail'),
   path('create', views.BlogPostCreateView.as_view(), name='post'),
   path('update/<int:pk>', views.BlogPostUpdateView.as_view(), name='update'),

   
#    path('detail/<int:myId>', views.detail, name='detail'),
#    path('delete/<int:id>', views.delete, name='delete'),
#    path('update/<int:id>', views.update, name='update'),

]

