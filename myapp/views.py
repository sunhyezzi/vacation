from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Myapp
from .forms import MyappForm
from .models import Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request): 
    return render(request, 'home.html')

@login_required
def index(request):
    myapps =Myapp.objects.order_by('-id') #쿼리셋
    return render(request, 'index.html', {'myapps':myapps})

@login_required
def detail(request, myapp_id):
    myapp_detail = get_object_or_404(Myapp, pk = myapp_id )
    return render(request, 'detail.html', {'myapp':myapp_detail})


@login_required
def new(request): #new.html 띄워주는 함수
    return render(request, 'new.html')

@login_required
def create(request): #입력받은 내용을 데이터베이스에 넣어주는 함수
    myapp = Myapp()
    myapp.title = request.GET['title']
    myapp.body = request.GET['body']
    myapp.update_date = timezone.datetime.now()
    myapp.save()
    return redirect('/myapp/' + str(myapp.id))

@login_required
def delete(request, pk):
        myapp = Myapp.objects.get(id=pk)
        myapp.delete()
        return redirect('index')

@login_required
def edit(request,pk):
        myapp = get_object_or_404(Myapp, pk=pk)

        if request.method == "POST":
                form = MyappForm(request.POST, instance=myapp)
             
                if form.is_valid():
                        myapp = form.save(commit = False)
                        myapp.update_date=timezone.now()
                        myapp.save()
                        return redirect('index')
        else:
                form = MyappForm(instance=myapp)
                return render(request, 'edit.html', {'form': form})


def detail(request, myapp_id):
        myapp = get_object_or_404(Myapp, pk=myapp_id)
        
        if request.method == "POST":
                comment_form = CommentForm(request.POST)
                comment_form.instance.myapp_id = myapp_id
                
                if comment_form.is_valid():
                        comment = comment_form.save()

        comment_form = CommentForm()
        comments = myapp.comments.all()

                       
        return render(request, 'detail.html', {'myapp':myapp, 'comments':comments, 'comment_form':comment_form})
