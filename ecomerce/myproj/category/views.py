from django.shortcuts import render,get_object_or_404
from . models import Category,product
# Create your views here.

def home(request):
    categories = Category.objects.all()
    products = product.objects.all()

    context = {
        'categories':categories,
        'products':products
    }
    return render (request, "index.html", context)

def category(request,category_id):
    
    category = get_object_or_404(Category,id=category_id)

    categories = Category.objects.all()
    products = product.objects.filter(category=category)
    
    context = {
        'categories':categories,
        'products':products,
        'category':category
    }
    return render(request, 'category.html',context )