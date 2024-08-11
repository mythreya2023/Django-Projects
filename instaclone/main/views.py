from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from main.models import post

# Create your views here.
def loginView(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        pwd = request.POST.get("pwd")
        check = authenticate(request,username=uname,password=pwd)
        if check:
            login(request,check)
            return redirect("homePage")
    return render(request,"login.html")

def registerView(request):
    if request.method == "POST":
        name=request.POST.get("name")
        mail=request.POST.get("email")
        uname = request.POST.get("uname")
        pwd = request.POST.get("pwd")
        obj = User.objects.create_user(email=mail,username=uname,password=pwd)
        obj.save()
        return redirect("profilePage")
    return render(request,"register.html")
    
def homeView(request):
    posts = post.objects.all()[::-1]
    return render(request,"home.html",{"posts":posts})

@login_required(login_url='loginPage')
def postView(request):
    if request.method == "POST":
        cont=request.POST.get('post')
        obj=post(uname=request.user.username,content=cont)
        obj.save()
        return redirect("homePage")
    return render(request,"posts.html")


@login_required(login_url='loginPage')
def updatePost(request,pid):
    res=post.objects.get(id=pid)
    if request.user.username == res.uname or request.user.is_superuser:
        if request.method == "POST":
            cont=request.POST.get('post')
            obj=post.objects.get(id=pid)
            obj.content=cont
            obj.save()
            return redirect("homePage")
        return render(request,"post.html",{"post":res})
    else:
        return redirect("homePage")


@login_required(login_url='loginPage')
def delPost(request,pid):
    obj=post.objects.get(id=pid)
    if request.user.username == obj.uname or request.user.is_superuser:
        obj.delete()
        return redirect("homePage")
    else:
        return redirect("homePage")


@login_required(login_url='loginPage')
def profileView(request):
    return render(request,"profile.html")

def logoutView(request):
    logout(request)
    return redirect("loginPage")
