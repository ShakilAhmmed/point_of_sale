from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from backend.models import Company

# Create your views here.
from product_template.models import ProductTemplate
from datetime import date
from django.db.models import Q
from purchase.models import PurchaseModel, PurchaseChildModel, PurchasePaymentModel, StockModel
from pos_section.models import CartProductModel
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
        quantity_sum = products.aggregate(quantity_sum=Sum('quantity'))
        purchase_sum = []
        sale_sum = []
        tax_sum = []
        for x in products:
            purchase_sum.append(x.product_name.product_cost_price * x.quantity)
            sale_sum.append(x.product_name.product_mrp * x.quantity)
            tax_sum.append(x.product_name.product_tax * x.quantity)

        context = {
            'values': request.POST,
            'product_data': products,
            'today': today,
            'count': count,
            'purchase_sum': sum(purchase_sum),
            'sale_sum': sum(sale_sum),
            'tax_sum': sum(tax_sum),
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


@login_required
def stock_report(request):
    if request.method == 'POST':
        today = date.today()
        all_data = request.POST.get('all_data', None)
        product_name = request.POST.get('product_name', None)
        status = request.POST.get('status', None)
        brand_name = request.POST.get('brand_name', None)
        stock_data = StockModel.objects.all()
        if all_data:
            if all_data.isnumeric():
                stock_data = stock_data.filter(
                    Q(product__product_code=all_data) | Q(product__product_mrp__lte=all_data) | Q(
                        product__product_cost_price__lte=all_data))
            else:
                stock_data = stock_data.filter(
                    Q(product__product_description__contains=all_data) | Q(stock_status__contains=all_data) | Q(
                        product__product_name=all_data))
        if brand_name:
            stock_data = stock_data.filter(product__product_brand_name=brand_name)
        if product_name:
            stock_data = stock_data.filter(product__id=product_name)
        if status:
            if status == 'Sold':
                stock_data = stock_data.filter(stock_status='Inactive')
            else:
                stock_data = stock_data.filter(stock_status='Active')
        count = stock_data.count()
        purchase_sum = stock_data.aggregate(purchase_sum=Sum('product__product_cost_price'))
        sale_sum = stock_data.aggregate(sale_sum=Sum('product__product_mrp'))
        tax_sum = stock_data.aggregate(tax_sum=Sum('product__product_tax'))
        context = {
            'values': request.POST,
            'count': count,
            'today': today,
            'stock_data': stock_data,
            'purchase_sum': purchase_sum,
            'sale_sum': sale_sum,
            'tax_sum': tax_sum
        }
        return render(request, 'backend/Reports/stock_report_show.html', context)
    else:
        company_data = Company.objects.all()
        product_data = ProductTemplate.objects.all()
        context = {
            'company_data': company_data,
            'product_data': product_data
        }
        return render(request, 'backend/Reports/stock_report_main.html', context)


@login_required
def sale_report(request):
    if request.method == 'POST':
        all_data = request.POST.get('all_data', None)
        product_name = request.POST.get('product_name', None)
        brand_name = request.POST.get('brand_name', None)
        from_date = request.POST.get('from_date', None)
        to_date = request.POST.get('to_date', None)
        sale_data = CartProductModel.objects.all()
        count = sale_data.count()
        today = date.today()
        if product_name:
            sale_data = sale_data.filter(product=product_name)
        if brand_name:
            sale_data = sale_data.filter(product__product_brand_name=brand_name)
        if from_date and to_date:
            sale_data = sale_data.filter(cart_parent__date__range=[from_date, to_date])
        if all_data:
            if all_data.isnumeric():
                sale_data = sale_data.filter(
                    Q(invoice_id=all_data) | Q(product_price__lte=all_data) | Q(product_quantity__lte=all_data))
            else:
                sale_data = sale_data.filter(product__product_name__contains=all_data)

        sale_sum = []
        for x in sale_data:
            sale_sum.append(int(x.product.product_mrp) * int(x.product_quantity))
        sub_total = sale_data.aggregate(sub_total_sum=Sum('product_subtotal'))
        quantity = sale_data.aggregate(quantity=Sum('product_quantity'))
        context = {
            'sale_data': sale_data,
            'count': count,
            'today': today,
            'values': request.POST,
            'sale_sum': sum(sale_sum),
            'sub_total': sub_total,
            'quantity': quantity
        }
        return render(request, 'backend/Reports/sale_report_show.html', context)
    else:
        company_data = Company.objects.all()
        product_data = ProductTemplate.objects.all()
        context = {
            'company_data': company_data,
            'product_data': product_data
        }
        return render(request, 'backend/Reports/sale_report_main.html', context)


@login_required
def profit_loss_report(request):
    if request.method == "POST":
        all_data = request.POST.get('all_data', None)
        product_name = request.POST.get('product_name', None)
        from_date = request.POST.get('from_date', None)
        to_date = request.POST.get('to_date', None)
        brand_name = request.POST.get('brand_name', None)
        profit_loss = StockModel.objects.all()
        if product_name:
            profit_loss = profit_loss.filter(product=product_name)
        if brand_name:
            profit_loss = profit_loss.filter(product__product_brand_name=brand_name)
        if from_date and to_date:
            profit_loss = profit_loss.filter(purchase__date__range=[from_date, to_date])
        count = profit_loss.count()
        today = date.today()
        purchase_sum = profit_loss.aggregate(purchase_sum=Sum('product__product_cost_price'))
        sale_sum = profit_loss.aggregate(sale_sum=Sum('product__product_mrp'))
        profit = int(sale_sum.get('sale_sum')) - int(purchase_sum.get('purchase_sum'))
        tax_sum = profit_loss.aggregate(tax_sum=Sum('product__product_tax'))
        stock_sale = profit_loss.filter(stock_status='Inactive').aggregate(stock_sale=Sum('product__product_mrp'))
        stock_purchase = profit_loss.filter(stock_status='Inactive').aggregate(
            stock_purchase=Sum('product__product_cost_price'))
        stock_profit = int(stock_sale.get('stock_sale')) - int(stock_purchase.get('stock_purchase'))
        context = {
            'profit_loss': profit_loss,
            'count': count,
            'today': today,
            'purchase_sum': purchase_sum,
            'sale_sum': sale_sum,
            'tax_sum': tax_sum,
            'profit': profit,
            'stock_sale': stock_sale,
            'stock_purchase': stock_purchase,
            'stock_profit': stock_profit
        }
        return render(request, 'backend/Reports/profit_loss_show.html', context)
    else:
        company_data = Company.objects.all()
        product_data = ProductTemplate.objects.all()
        context = {
            'company_data': company_data,
            'product_data': product_data
        }
        return render(request, 'backend/Reports/profit_loss_main.html', context)
