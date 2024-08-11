from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from menu.models import dinner,notePad


# Create your views here.

def allFoods(request):
    return render(request,'index.html',{"foods":dinner.objects.all()})

def food(request):
    results = dinner.objects.all()
    if request.method=="POST" and request.POST.get("food_price"):
        dish=request.POST.get("food")
        price=request.POST.get("food_price")
        cat=request.POST.get("category")
        obj = dinner(name=dish,price=price,category=cat)
        obj.save()
        results = dinner.objects.all()
    elif request.method=="POST":
        dish=request.POST.get("food")
        results = dinner.objects.filter(name=dish)
        if results.exists() == False:
            results = None;
    
    
    return render(request,'food.html',{"foods":results})

def edit(request):
    # results=
    if request.method=="GET" and request.GET.get("op")=="upd":
        sno=request.GET.get("id")
        dish=request.GET.get("name")
        price=request.GET.get("price")
        cat=request.GET.get("cat")
        obj = dinner.objects.get(id=sno)
        obj.name=dish
        obj.price=price
        obj.category=cat
        obj.save()
        return HttpResponse("Edited Successfully!")
    elif request.method=="GET" and request.GET.get("op")=="del":
        sno=request.GET.get("id")
        obj = dinner.objects.get(id=sno)
        obj.delete()
        return HttpResponse("Deleted Successfully!")
    return HttpResponse("Hello!")

def notes(request,id):
    result = None
    if notePad.objects.filter(id=id).exists():
        result = notePad.objects.get(id=id)
   
    return render(request,"notes.html",{"pad":result})

def allnotes(request):
    result = notePad.objects.all()
     
    return render(request,"allnotes.html",{"pad":result})


def notesUpd(request):
    if request.method=="GET" and request.GET.get("op")=="create":
        obj = notePad(title="Untitled",content="Enter Your Content...")
        obj.save()
        return HttpResponse(obj.id)
    if request.method=="GET" and request.GET.get("op")=="save":
        sno=request.GET.get("id")
        txt=request.GET.get("txt")
        fname=request.GET.get("name")
        obj = notePad.objects.get(id=sno)
        obj.content=txt
        obj.title=fname
        obj.save()
        return HttpResponse("Saved Successfully!")
    elif request.method=="GET" and request.GET.get("op")=="del":
        sno=request.GET.get("sno")
        obj = notePad.objects.get(id=sno)
        obj.delete()
        return HttpResponse("Deleted Successfully!")
