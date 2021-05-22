"""albamon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from albamon_app.views import main,detail,post_page,post,update_page,update,delete,plus,minus

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main,name='main'),
    path('detail/<int:id>/',detail,name='detail'),
    path('post_page/',post_page,name='post_page'),
    path('post/',post,name='post'),
    path('update_page/<int:id>/',update_page,name='update_page'),
    path('update/<int:id>/',update,name='update'),
    path('delete/<int:id>/',delete,name='delete'),
    path('plus/<int:id>/',plus,name='plus'),
    path('minus/<int:id>/',minus,name='minus'),
]
