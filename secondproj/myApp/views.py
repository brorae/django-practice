from django.shortcuts import get_object_or_404, render
from .models import Blog, Comment
from .models import Team
# Create your views here.

def main(request):
    return render(request,'main.html')

def home(request):
    blogs = Blog.objects.all() #Blog 테이블에 있는 오브젝트 모두를 불러오기.
    return render(request, 'home.html', {'blogs':blogs}) #home.html 과 함께 blogs를 보내준다.

def team(request):
    teams = Team.objects.all()
    return render(request,'team.html',{'teams':teams})

def detail(request,id):
    detail_data = get_object_or_404(Blog,pk = id)
    comments = Comment.objects.filter(blog_id = id)
    context = {
        'title' : detail_data.title,
        'writer' : detail_data.writer,
        'body' : detail_data.body,
        'pub_date' : detail_data.pub_date,
        'id' : id,
        'comments' : comments
    }