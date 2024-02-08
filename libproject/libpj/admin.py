from django.contrib import admin
from .models import Profile, Pwdlist, Book

# Register your models here.
admin.site.register(Profile)
admin.site.register(Pwdlist)
admin.site.register(Book)