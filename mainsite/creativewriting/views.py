from django.shortcuts import render,redirect
from django.utils import timezone
from django.http import HttpResponse
from .models import Articles
from .forms import ArticlePost,Register
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def writing_index(request):
    all_articles = Articles.objects.all()
    return render(request,'creativewriting/writingindex.html',{'articles':all_articles})
def index(request):
    return render(request,'creativewriting/index.html',{})

def post_article(request):
    if request.method == 'POST':
        form = ArticlePost(request.POST)
        if(form.is_valid()):
            article = form.save(commit=False)
            article.author = request.user.username
            article.datecreated = timezone.now()
            article.datemodified = timezone.now()
            article.save()
            return redirect('writing_index')
    else:
        form = ArticlePost()
        return render(request,'creativewriting/submit_articles.html',{'form':form})

def register(request):

    if request.method == 'POST':
        form = Register(request.POST)
        if(form.is_valid()):
            user = form.save(commit=False)
            ## do any modifications to inputted data here
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(user.password)  ##important
            user.save()

            ##keep them logged in after registering
            user = authenticate(username = username,password = password)

            if user is not None: ##that the user does exist in the database
                if user.is_active:
                    login(request,user)
                    return redirect('writing_index')
                else:
                    return redirect('writing_index')

    else:
        form = Register()
        return render(request,'creativewriting/register.html',{'form':form})

def Login(request):
     if request.method == 'POST':
         username = request.POST.get('username')
         password = request.POST.get('password')
         user = authenticate(username=username, password=password)
         if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('writing_index')
            else:
                return HttpResponse("Your account was inactive.")
         else:
            return HttpResponse("Invalid login details given")
     else:
        return render(request, 'creativewriting/login.html', {})

def Logout(request):
    logout(request)
    return render(request,'creativewriting/index.html',{})