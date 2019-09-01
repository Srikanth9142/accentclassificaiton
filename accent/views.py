from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'accent/index.html')

def testing(request):
    return HttpResponse('This is another view ')

