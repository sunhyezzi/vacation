from django import forms
from .models import Myapp, Comment

 class Create(forms.ModelForm):
    class Meta:
        model = Myapp
        fields = ['title', 'body']

 class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 40})
        }

     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].label = '댓글
        