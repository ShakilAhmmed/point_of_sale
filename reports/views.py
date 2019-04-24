from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from backend.models import Company

# Create your views here.
from product_template.models import ProductTemplate
from datetime import date
from django.db.models import Q


@login_required
def products_report(request):
    if request.method == 'POST':
        all_data = request.POST.get('all_data', None)
        brand = request.POST.get('brand', None)
        status = request.POST.get('status', None)
        act = request.POST.get('act', None)
        today = date.today()
        product_data = ProductTemplate.objects.all()
        if brand:
            product_data = product_data.filter(product_brand_name=brand)
        if status:
            product_data = product_data.filter(product_status=status)
        if act:
            product_data = product_data.filter(is_published=act)
        if all_data:
            if all_data.isnumeric():
                product_data = product_data.filter(
                    Q(product_cost_price__lte=all_data) | Q(product_mrp__lte=all_data) | Q(product_code=all_data))
            else:
                product_data = product_data.filter(
                    Q(product_mrp__contains=all_data) | Q(product_description__contains=all_data))
        count = product_data.count()
        context = {
            'values': request.POST,
            'product_data': product_data,
            'today': today,
            'count': count
        }
        return render(request, 'backend/Reports/products_report_data.html', context);
    else:
        company_data = Company.objects.all()
        context = {
            'company_data': company_data
        }
        return render(request, 'backend/Reports/products_report.html', context)
