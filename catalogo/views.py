from django.shortcuts import render

from .models import Product, Category

# Create your views here.

def product_list(request):
	context = {
		'products': Product.objects.all()

	}
	return render(request, 'catalogo/products.html', context)

def category(request, slug):
	category = Category.objects.get(slug=slug)
	context = {
		'current_category':category,
		'product_list':Product.objects.filter(category=category),


	}
	return render(request, 'catalogo/category.html', context)	

def product(request, slug):
	product = Product.objects.get(slug=slug)
	context = { 
		'product': product
	}
	return render(request, 'catalogo/product.html', context)
