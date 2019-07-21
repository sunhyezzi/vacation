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
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name='comments')
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_contents = models.CharField(max_length=200)
    text = models.TextField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return (self.author.username if self.author else "무명")+ "의 댓글"


