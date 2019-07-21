from django.db import models

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
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

    def __str__(self):
        return (self.author.username if self.author else "무명")+ "의 댓글"
