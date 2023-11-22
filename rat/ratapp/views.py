from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def demo(request):
#     return HttpResponse("hai man")
from.models import place
from.models import pho
def demo(request):
    obj=place.objects.all()
    # hat="ajpan"
    ob = pho.objects.all()
    # hat="ajpan"
    return render(request,"index.html",{'result':obj,'res': ob})

# def addition(request):

#     x=int(request.GET['name1'])
#     y=int(request.GET['name2'])
#     m=x+y
#     return render(request,"add.html",{'n':m})