from os import name
from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
#    path('detail/<int:myId>', views.detail, name='detail'),
#    path('delete/<int:id>', views.delete, name='delete'),
#    path('update/<int:id>', views.update, name='update'),

]

