from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request -> response
# request render
# action 

def say_hello(request):
    #The following things can be done in this function
    #Pull data from a database
    #Transform the data
    #Send emails
    return render(request,'hello.html',{'name':'Tanya'})