from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from api.models import Product, Category

def list_of_all_prod(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)

def list_of_all_categories(request):
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False)

Products = [
    {
        'id': i,
        'name': f'Product {i}',
        'price': i * 1000,
        'category': f'Category {i}',
    }
    for i in range(1, 10)
]

Categories = [
    {
        'id': i,
        'name': f'Category {i}',
    }
    for i in range(1, 10)
]


def list_of_all_prod(request):
    return JsonResponse(Products, safe=False)

def product_detail(request, product_id):
    for product in Products:
        if product['id'] == product_id:
            return JsonResponse(product, status=200)
    return JsonResponse({'message': 'Product not found with selected ID'}, status=400)

def list_of_all_categories(request):
    return JsonResponse(Categories, safe=False)

def category_detail(request, category_id):
    for category in Categories:
        if category['id'] == category_id:
            return JsonResponse(category, status=200)
    return JsonResponse({'message': 'Category not found with selected ID'}, status=400)

def product_by_category(request, category_id):
    for product in Products:
        for category in Categories:
            if category['id'] == category_id:
                return JsonResponse(product, status=200)