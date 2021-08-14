from os import name
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
   path('', views.home, name='home'),
   path('detail/<int:myId>', views.detail, name='detail'),
   path('delete/<int:id>', views.delete, name='delete'),
   path('update/<int:id>', views.update, name='update'),
   path('about', views.about, name='about'),
   path('contact', views.contact, name="contact"),
   path('account/', views.account, name="account"),
   path('login/', LoginView.as_view(template_name='crud/login.html'), name="login"),
   path('logout/', LogoutView.as_view(template_name='crud/logout.html'), name="logout"),

]


