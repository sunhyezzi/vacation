from django import forms
from .models import Myapp, Comment

 class Create(forms.ModelForm):
    class Meta:
        model = Myapp
        fields = ['title', 'body']

 class MyappCommentForm(forms.ModelForm): 
    class Meta: 
        model = Comment 
        fields = ['comment_user', 'comment_textfield'] 
        widgets = { 
            'comment_textfield' : forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 40}) 
        } 
        