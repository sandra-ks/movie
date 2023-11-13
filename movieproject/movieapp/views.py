from django.http import HttpResponse
from django.shortcuts import render, redirect

from movieapp import models
from .forms import MovieForm
from .models import movie

# Create your views here.
def index(request):
    film=movie.objects.all()
    context={
        'movie_list':film
    }
    return render(request,'index.html',context)

def detail(request,movie_id):
    Movie=movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movies':Movie})
def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        img = request.FILES['img']
        cinema=movie(name=name,desc=desc,year=year,img=img)
        cinema.save()

    return render(request,'add.html')
def update(request,id):
    Movie=movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=Movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':Movie})

def delete(request,id):
    if request.method=='POST':
        Movie=movie.objects.get(id=id)
        Movie.delete()
        return redirect('/')
    return render(request,'delete.html')