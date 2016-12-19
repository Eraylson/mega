from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from catalogo.models import Category

def index(request):
	#context = {
	#'categories': Category.objects.all()
	#}

	return render(request,'index.html')

def contact(request):
	return render(request,'contact.html')

