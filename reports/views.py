from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from backend.models import Company

# Create your views here.
from product_template.models import ProductTemplate
from datetime import date
from django.db.models import Q
from purchase.models import PurchaseModel, PurchaseChildModel, PurchasePaymentModel
from django.db.models import Sum


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


@login_required
def purchase_full_report(request):
    if request.method == 'POST':
        today = date.today()
        all_data = request.POST.get('all_data', None)
        product_name = request.POST.get('product_name', None)
        status = request.POST.get('status', None)
        from_date = request.POST.get('from_date', None)
        to_date = request.POST.get('to_date', None)
        brand_name = request.POST.get('brand_name', None)
        pay_status = request.POST.get('pay_status', None)
        products = PurchaseChildModel.objects.all()
        if product_name:
            products = products.filter(product_name=product_name)
        if brand_name:
            products = products.filter(purchase__company_name=brand_name)
        if status:
            products = products.filter(product_name__product_status=status)
        if from_date and to_date:
            products = products.filter(purchase__date__range=[from_date, to_date])
        if all_data:
            if all_data.isnumeric():
                products = products.filter(
                    Q(product_name__product_cost_price__lte=all_data) | Q(product_name__product_mrp__lte=all_data) | Q(
                        product_name__product_code=all_data))
            else:
                products = products.filter(
                    Q(product_name__product_mrp__contains=all_data) | Q(
                        product_name__product_description__contains=all_data))
        count = products.count()
        purchase_sum = products.aggregate(purchase_sum=Sum('product_name__product_cost_price'))
        sale_sum = products.aggregate(sale_sum=Sum('product_name__product_mrp'))
        tax_sum = products.aggregate(tax_sum=Sum('product_name__product_tax'))
        quantity_sum = products.aggregate(quantity_sum=Sum('quantity'))

        context = {
            'values': request.POST,
            'product_data': products,
            'today': today,
            'count': count,
            'purchase_sum': purchase_sum,
            'sale_sum': sale_sum,
            'tax_sum': tax_sum,
            'quantity_sum': quantity_sum
        }
        return render(request, 'backend/Reports/purchase_reports_show.html', context);

    else:
        product_data = ProductTemplate.objects.all()
        company_data = Company.objects.all()
        context = {
            'product_data': product_data,
            'company_data': company_data
        }
        return render(request, 'backend/Reports/purchase_report.html', context)
