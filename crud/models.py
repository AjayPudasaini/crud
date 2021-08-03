from django.db import models

# Create your models here.

class Student(models.Model):
    username = models.CharField(max_length=500, verbose_name="Usename", help_text="enter username")
    email = models.EmailField(max_length=500, verbose_name="Email", help_text="enter email")
    address = models.CharField(max_length=500, verbose_name="Address", help_text="enter address")

    def __str__(self):
        return self.username


