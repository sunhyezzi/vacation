from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.
class Myapp(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:50]


class Comment(models.Model):
 
    Myapp = models.ForeignKey(Myapp, on_delete=models.CASCADE, null=True, related_name='comments')
    comment_user = models.CharField(max_length=200, null=True)
    comment_date = models.DateTimeField(auto_now_add=True, null=True)
    comment_textfield = models.TextField()
