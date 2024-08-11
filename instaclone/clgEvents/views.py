from django.shortcuts import render,redirect
from clgEvents.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def displayEve(request):
    evs = Event.objects.all()[::-1]
    usr = request.user
    if request.user.is_authenticated:
        for even in evs:
            regusr = RegEvent.objects.filter(event=even,user=usr)
            if regusr.exists():
                for rgu in regusr:
                    if even.id == rgu.event.id:
                        even.isReg = 1
            else:
                even.isReg = 0  

    if request.method == "POST" and request.POST.get("search"):
        srch = request.POST.get("search")
        evs = Event.objects.filter(eveName__icontains=srch)[::-1]
        # return redirect("EventsPage")
    elif request.method == "POST" and request.POST.get("unreg"):
        evId = int(request.POST.get("unreg"))
        eve = Event.objects.get(id=evId)
        obj = RegEvent.objects.get(event=eve,user=usr)
        obj.delete()
        return redirect("EventsPage")
    elif request.method == "POST":
        evId = int(request.POST.get("eveId"))
        eve = Event.objects.get(id=evId)
        obj = RegEvent(event=eve,user=usr)
        obj.save()
        return redirect("EventsPage")
    
    return render(request,'display_eve.html',{"events":evs})


@login_required(login_url="http://127.0.0.1:8000/login")
def createEve(request):
    if request.method == "POST":
        evePic = request.FILES.get('Img')
        evname = request.POST.get("eveName")
        evDesc = request.POST.get("eveDesc")
        evDate = request.POST.get("eveDate")
        evBranch = request.POST.get("eveBranch")
        evYear = int(request.POST.get("eveYear"))
        obj = Event(eveName=evname,eveDesc=evDesc,eveDate=evDate,eveImg=evePic,eveBranch=evBranch,eveYear=evYear)
        obj.save()
        return redirect("EventsPage")
    return render(request,'create_event.html')