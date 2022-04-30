import json

from django.http.response import JsonResponse
from django.shortcuts import render
from api.models import Company, Vacancy
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def company_list(request):
    companies = Company.objects.all()
    companies_json = [company.to_json() for company in companies]
    return JsonResponse(companies_json, safe=False)

def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    return JsonResponse(company.to_json())

@csrf_exempt
def company_list1(request):
    if request.method == 'GET':
        companies = Company.objects.filter(name__contains='5').order_by('-salary')
        companies_json = [company.to_json() for company in companies]
        return JsonResponse(companies_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        try:
            company = Company.objects.create(name=data['name'])
        except Exception as e:
            return JsonResponse({'message': str(e)})

        return JsonResponse(company.to_json())

@csrf_exempt
def company_detail1(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    if request.method == 'GET':
        return JsonResponse(company.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        company.name = data['name']
        company.save()
        return JsonResponse(company.to_json())
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({'message': 'deleted'}, status=204)

companies = [
    {
        'id': i,
        'name': f'Company {i}',
        'description': '',
        'city': f'City {i}',
        'address': f'Address {i}'
    }
    for i in range(1, 10)
]


def company_list(request):
    return JsonResponse(companies, safe=False)


def company_detail(request, company_id):
    for company in companies:
        if company['id'] == company_id:
            return JsonResponse(company, status=200)
    return JsonResponse({'message': 'Company not found with selected ID'}, status=400)

def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)

def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    return JsonResponse(vacancy.to_json())

vacancies = [
    {
        'id': i,
        'name': f'Company {i}',
        'description': '',
        'salary': i * 1000,
        'company': f'Company {i}'
    }
    for i in range(1, 10)
]


def vacancy_list(request):
    return JsonResponse(vacancies, safe=False)


def vacancy_detail(request, vacancy_id):
    for vacancy in vacancies:
        if vacancy['id'] == vacancy_id:
            return JsonResponse(vacancy, status=200)
    return JsonResponse({'message': 'Vacancy not found with selected ID'}, status=400)