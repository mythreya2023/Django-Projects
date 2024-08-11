from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request,name):
    rhym = """<p>
        <b>Father:</b> {}, {}<br>
        <b>{}:</b> Yes, papa<br>
        <b>Father:</b> Eating sugar?<br>
        <b>{}:</b> No, papa<br>
        <b>Father:</b> Telling lies?<br>
        <b>{}:</b> No, papa<br>
        <b>Father:</b> Open your mouth<br>
        <b>{}:</b> Ah, ah, ah</p>
    """
    return HttpResponse(rhym.format(name,name,name,name,name,name))

