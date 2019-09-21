from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from purchase.models import PurchaseModel, PurchaseChildModel, PurchasePaymentModel, StockModel
from django.db.models import Sum, Count
from product_template.models import ProductTemplate


# Create your views here.
@login_required
def stock_data(request):
    purchase_data_grp = PurchaseChildModel.objects.values('product_name_id').annotate(qty=Sum('quantity'))
    stock_data_grp = StockModel.objects.values('product_id').filter(stock_status='Active').annotate(
        stock=Count('stock_code'))
    total_stock_data = StockModel.objects.values('product_id').filter(stock_status='Active').aggregate(
        stock=Count('stock_code'))
    total_sale_data = StockModel.objects.values('product_id').filter(stock_status='Inactive').aggregate(
        total_sale=Count('stock_code'))
    total_sale = StockModel.objects.values('product_id').filter(stock_status='Inactive').annotate(
        sale=Count('stock_code'))
    total_purchase_data = PurchaseChildModel.objects.values('product_name_id').aggregate(qty=Sum('quantity'))
    purchase_main_data = ProductTemplate.objects.all()
    print(total_sale)
    context = {
        'purchase_data_grp': purchase_data_grp,
        'purchase_main_data': purchase_main_data,
        'stock_data_grp': stock_data_grp,
        'total_stock_data': total_stock_data,
        'total_purchase_data': total_purchase_data,
        'total_sale': total_sale,
        'total_sale_data': total_sale_data
    }
    return render(request, 'backend/Stock/stock_data.html', context)
