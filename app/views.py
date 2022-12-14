from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
def display_topic(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    LWO=Webpage.objects.all()
    LWO=Webpage.objects.filter(name='MSD')
    LWO=Webpage.objects.exclude(name='MSD')
    LWO=Webpage.objects.all()[2:5:]
    LWO=Webpage.objects.filter(name='MSD').order_by('-url')
    LWO=Webpage.objects.all().order_by(Length('url'))
    LWO=Webpage.objects.all().order_by(Length('url').desc())
    LWO=Webpage.objects.filter(name__startswith='s')
    LWO=Webpage.objects.filter(name__endswith='l')
    LWO=Webpage.objects.filter(name__contains='s')
    LWO=Webpage.objects.filter(name__in=('pradeep','MSD'))
    LWO=Webpage.objects.filter(name__regex='M\w{4}')
    LWO=Webpage.objects.all()
    d={'LWO':LWO}
    return render(request,'display_webpage.html',d)

def display_access(request):
    LAO=AccessRecords.objects.all()
    LAO=AccessRecords.objects.filter(date__year='2001')
    LAO=AccessRecords.objects.filter(date__month='8')
    LAO=AccessRecords.objects.filter(date__day='19')
    LAO=AccessRecords.objects.filter(date__year__gte='2001')
    LAO=AccessRecords.objects.filter(date__year__lte='2001')
    LAO=AccessRecords.objects.all()

    d={'LAO':LAO}
    return render(request,'display_access.html',d)