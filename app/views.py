from django.shortcuts import render
from app.models import *

# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        to=Topic.objects.get_or_create(topic_name=tn)[0]
        to.save()
        QLTO=Topic.objects.all()
        return render(request,'display_topic.html',{'Topics':QLTO})
    
    return render(request,'insert_topic.html')
def insert_webpage(request):
    QLTO=Topic.objects.all()
    d={'Topics': QLTO}
    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        em=request.POST['em']
        TO=Topic.objects.get(topic_name=tn)
        wo=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur,email=em)[0]
        wo.save()
        QLWO=Webpage.objects.all()
        d1={'webpages':QLWO}
        return render(request,'display_webpages.html',d1)
    return render(request,'insert_Webpage.html',d) 

def insert_acess(request):
    QLWO=Webpage.objects.all()
    d={'Webpages':QLWO}
    if request.method=='POST':
        na=request.POST['na']
        au=request.POST['au']
        da=request.POST['da']
        wo=Webpage.objects.get(name=na)
        ao=AcessRecords.objects.get_or_create(name=wo,author=au,date=da)[0]
        ao.save()
        QLAO=AcessRecords.objects.all()
        d1={'acess':QLAO}
        return render(request,'display_acess.html',d1)
    return render(request,'insert_acess.html',d)

def select_multiple_webpages(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}

    if request.method=='POST':
        topiclist=request.POST.getlist('tn')
        QLWO=Webpage.objects.none()
        for i in topiclist:
            QLWO=QLWO|Webpage.objects.filter(topic_name=i)

        d1={'webpages':QLWO}
        return render(request,'display_webpages.html',d1) 

    return render(request,'select_multiple_webpages.html',d)



def checkbox(request):
    QLTO=Topic.objects.all()
    d={'topics': QLTO}
    return render(request,'checkbox.html',d)