from django.shortcuts import render, get_object_or_404, redirect
from .models import Company


def get_all_companies(request):
    context = {
        'company': Company.objects.all()
    }
    return render(request, 'company/get_all_companies.html', context)


def company_by_id(request, id=0):
    company_by_id = Company.objects.get(id=id)
    return render(request, 'company/get-company.html', {'title': "Company by id", "company_by_id": company_by_id})



