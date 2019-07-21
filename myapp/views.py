from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Myapp, Comment
from .forms import CommentForm


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

def comment_write(request, post_pk):
    if request.method == "POST":
        post = get_object_or_404(Post, pk=post_pk)
        content = request.POST.get('content')

        conn_user = request.user
        conn_profile = Profile.objects.get(user=conn_user)

        if not content:
            messages.info(request, '님 아무것도 안 썼는디요' )
            return HttpResponseRedirect(reverse_lazy('post:detail', post_pk))

        Comment.objects.create(post=post, comment_writer=conn_profile, comment_contents=content)
        return HttpResponseRedirect(reverse_lazy('myapp_index'))

