from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Myapp, Comment
from .forms import  Create, MyappCommentForm
from django.http import HttpResponseRedirect
from django import forms

# Create your views here.

def home(request): 
    return render(request, 'home.html')

def index(request):
    myapps =Myapp.objects #쿼리셋
    return render(request, 'index.html', {'myapps':myapps})

def detail(request, myapp_id):
    myapp_detail = get_object_or_404(Myapp, pk = myapp_id )
    return render(request, 'detail.html', {'myapp':myapp_detail})

def new(request): #new.html 띄워주는 함수
    return render(request, 'new.html')

def create(request): #입력받은 내용을 데이터베이스에 넣어주는 함수
    myapp = Myapp()
    myapp.title = request.GET['title']
    myapp.body = request.GET['body']
    myapp.update_date = timezone.datetime.now()
    myapp.save()
    return redirect('/myapp/' + str(myapp.id))

def delete(request, pk):
        myapp = Myapp.objects.get(id=pk)
        myapp.delete()
        return redirect('index')


def comment(request, blog_id):
    blog_detail = get_object_or_404(Myapp, pk = blog_id)
    comments = Comment.objects.filter(blog_id=blog_id)

    if request.method == 'POST':
        comment_form = MyappCommentForm(request.POST)
        comment_form.instance.blog_id = blog_id
        if comment_form.is_valid():
            comment_form.save()
  
    else :
        comment_form = MyappCommentForm()

    context = {
            'blog_detail' : blog_detail,
            'comments': comments,
            'comment_form': comment_form
            
    }
    return render(request, 'myapp/index.html', context)

def comment_delete(request, pk) :
    comment = get_object_or_404(Comment, pk = pk)
    comment.delete()
    return redirect('home')

def comment_update(request, pk):
    comment = get_object_or_404(Comment, pk = pk)
    form = MyappCommentForm(request.POST, instance = comment)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'myapp/comment.html', {'form' : form})