from django.http import HttpResponse
from django.shortcuts import render

def home_view(*args,**kwargs):
	print(args,kwargs)
	print(request.user)
	return render(request, "home.html",{})

def contact_view(*args,**kwargs):
	return HttpResponse("<h1>Contacts</h1>")

def about_view(*args,**kwargs):
	return HttpResponse("<h1>About</h1>")

def gallery_view(*args,**kwargs):
	return HttpResponse("<h1>Gallery</h1>")
# Create your views here.
