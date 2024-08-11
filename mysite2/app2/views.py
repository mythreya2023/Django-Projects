from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

# Create your views here.

def home(request,num):
    
    context={
        "even":num%2==0,
    }
    return render(request,"index.html",context)

def contact(request):
    return render(request,'contact.html')

def trains(request):
    return render(request,'trains.html')

def hotel(request):
    return render(request,'hotel.html')

def flights(request):
    return render(request,'flights.html')

def bus(request):
    return render(request,'bus.html')

def about(request):
    return render(request,'about.html')

def search(request):
    return render(request,'prime.html')

def actor(request,hero):
    movie = {
        "ram charan":{
            "actor":"Ram Charan",
            "movies":["Chirutha (2007) - Blockbuster",
                    "Magadheera (2009) - All Time Blockbuster",
                    "Orange (2010) - Disaster",
                    "Racha (2012) - Super Hit",
                    "Naayak (2013) - Hit",
                    "Zanjeer (2013) - Flop (Bollywood debut)",
                    "Yevadu (2014) - Hit"]},
        "allu arjun":{"actor":"Allu Arjun","movies":["Arya (2004) - Super Hit","Bunny (2005) - Super Hit","Julayi (2012) - Super Hit","Race Gurram (2014) - Blockbuster","Pushpa: The Rise (2021) - Blockbuster"]},
        "mahesh babu":{"actor":"Mahesh Babu","movies":["Okkadu (2003) - Blockbuster","Pokiri (2006) - Blockbuster","Dookudu (2011) - Blockbuster","Srimanthudu (2015) - Blockbuster","Bharat Ane Nenu (2018) - Super Hit"]},
        "prabhas":{"actor":"Prabhas","movies":[
            "Baahubali: The Beginning (2015) ",
            "Baahubali 2: The Conclusion (2017)","Salaar: Part 1 – Ceasefire (2023)","Chatrapathi (2005)","Mirchi (2013)","Saaho (2019)"
        ]}
    }
    
    
    # result += "<br><a href='http://127.0.0.1:8000/app2/'>Search Other Actors</a>"
    return JsonResponse(movie[hero])