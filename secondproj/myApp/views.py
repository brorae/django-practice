from django.shortcuts import render
from .models import Blog
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