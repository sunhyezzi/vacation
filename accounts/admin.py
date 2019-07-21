from django.contrib import admin
from .models import Myapp, Post
# Register your models here.
admin.site.register(Myapp, Post)

