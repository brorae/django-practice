from django.shortcuts import get_object_or_404, render, redirect
from .models import Job
# Create your views here.

def main(request):
    jobs = Job.objects.all()
    context = {
        'jobs' : jobs
    }
    return render(request,'main.html',context)

def detail(request,id):
    detail_data = get_object_or_404(Job,pk=id)
    context = {
        'name' : detail_data.name,
        'location' : detail_data.location,
        'information' : detail_data.information,
        'pay' : detail_data.pay,
        'work' : detail_data.work,
        'applier' : detail_data.applier,
        'id' : id,
    }
    return render(request,'detail.html',context)

def post_page(request):
    return render(request,'post.html')

def post(request):
    new_data = Job()
    new_data.name = request.POST['name'] 
    new_data.location = request.POST['location']
    new_data.information = request.POST['information']
    new_data.pay = request.POST['pay']
    new_data.work = request.POST['work']
    new_data.applier = request.POST['applier']
    new_data.save()
    return redirect('main')

def update_page(request,id):
    update_data = get_object_or_404(Job, pk=id)
    context = {
        'name':update_data.name,
        'location':update_data.location,
        'information':update_data.information,
        'pay':update_data.pay,
        'work':update_data.work,
        'applier':update_data.applier,
        'id':id,
    }
    return render(request,'update.html',context)

def update(request, id):
    update_data = get_object_or_404(Job, pk=id)
    update_data.name = request.POST['name'] 
    update_data.location = request.POST['location']
    update_data.information = request.POST['information']
    update_data.pay = request.POST['pay']
    update_data.work = request.POST['work']
    update_data.applier = request.POST['applier']
    update_data.save()
    return redirect('main')

def delete(request, id):
    delete_data = get_object_or_404(Job, pk=id)
    delete_data.delete()
    return redirect('main') 

def plus(request,id):
    data = get_object_or_404(Job, pk=id)
    data.applier += 1
    data.save()
    return redirect('detail',id)

def minus(request,id):
    data = get_object_or_404(Job, pk=id)
    data.applier -= 1
    data.save()
    return redirect('detail',id)




