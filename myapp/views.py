from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def TextFun(request):
    return HttpResponse('this our views hello page')
def IndexFun(request):
    return render(request,'index.html')
