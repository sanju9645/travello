from django.shortcuts import render
from .models import destination

# Create your views here.

def index(request):

    dest1 = destination()
    dest1.name="Mumbai"
    dest1.price=800
    dest1.desc="asdfffgggjjgjgjg"
    dest1.img="destination_6.jpg"

    dest2 = destination()
    dest2.name="Calicut"
    dest2.price=1000
    dest2.desc="hfuherfuurfugrfrgfrg"
    dest2.img="destination_5.jpg"

    dest3 = destination()
    dest3.name="Wayanad"
    dest3.price=1200
    dest3.desc="iurfigrfgrfubrubvr"
    dest3.img="destination_4.jpg"

    dest4 = destination()
    dest4.name="Kannur"
    dest4.price=850
    dest4.desc="asdfffgggrfrfrfrfrfrfrfjjgjgjg"
    dest4.img="destination_3.jpg"

    dest5 = destination()
    dest5.name="Malappuram"
    dest5.price=8000
    dest5.desc="wsdwwswswswswswswswswsw"
    dest5.img="destination_2.jpg"

    dest6 = destination()
    dest6.name="Kottayam"
    dest6.price=400
    dest6.desc="asassasasasasasasasasasasasg"
    dest6.img="destination_1.jpg"

    dests=[dest1,dest2,dest3,dest4,dest5,dest6]

    return render(request,'index.html',{'dests' : dests})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def destinations(request):
    return render(request,'destinations.html')

def elements(request):
    return render(request,'elements.html')

def news(request):
    return render(request,'news.html')
