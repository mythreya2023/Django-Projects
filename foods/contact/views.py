from django.shortcuts import render

# Create your views here.
def notifyAdmin(request):
    return render(request,'n_admin.html')

def notifyUser(request):
    return render(request,'n_user.html')