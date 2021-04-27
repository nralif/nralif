from django.shortcuts import render

from .models import profile
# Create your views here.

def homepage(request):

    Profile= profile.objects.all()

    context={
        'profile':Profile        
    }

    return render(request,'index.html',context)
