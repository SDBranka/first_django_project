from django.shortcuts import redirect, render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs" )
    
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog" )

def create(request):
    return redirect('/')    #for redirects you must start off the string with a /

def show(request, number):
    return HttpResponse(f"placeholder to display blog number: {number}" )

def edit(request, number):
    return HttpResponse(f"placeholder to edit blog number: {number}" )

def destroy(request, number):
    return redirect('/')