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


def comment(request, document_id):

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        comment_form.instance.author_id = request.user.id
        comment_form.instance.document_id = document_id
        if comment_form.is_valid():
            comment = comment_form.save()

    return HttpResponseRedirect(reverse_lazy('board:detail', args=[document_id]))

# get_absolute_url을 설정해 놓았을 시(in models)
    def get_absolute_url(self):
        return reverse('board:detail', args=[self.id])