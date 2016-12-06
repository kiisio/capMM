from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'index.html')
		
def plans(request):
	return render(request, 'plans.html')
	
def cours(request):
	return render(request, 'cours.html')
