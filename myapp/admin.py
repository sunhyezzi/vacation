from django.contrib import admin
from .models import Myapp
from .models import Comment

# Register your models here.
admin.site.register(Myapp)
admin.site.register(Comment)

