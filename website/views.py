

from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse
from Test_Meeting.models import Meeting

def welcome(request):
    if request.user.is_authenticated:
        context={"meetings":Meeting.objects.all()}
    else:
        context={}
    return render(request, 'website/welcome.html',
                  context)
