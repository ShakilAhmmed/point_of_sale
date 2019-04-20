from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from purchase.forms.purchase import PurchaseForm
from .models import PurchaseModel, PurchaseChildModel, PurchasePaymentModel, StockModel
from product_template.models import ProductTemplate
import time


@login_required
def purchase(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        product_name = request.POST.getlist('product_name[]')
        quantity = request.POST.getlist('quantity[]')
        total = request.POST.get('total')
        pay = request.POST.get('pay')
        if form.is_valid():
            purchase = form.save()
            if product_name and quantity:
                for i in range(len(product_name)):
                    product_get = get_object_or_404(ProductTemplate, pk=product_name[i])
                    purchase_child = PurchaseChildModel()
                    purchase_child.purchase = purchase
                    purchase_child.product_name = product_get
                    purchase_child.quantity = quantity[i]
                    sub_total = int(product_get.product_cost_price) * int(quantity[i])
                    purchase_child.sub_total = sub_total
                    purchase_child.save()
                    print(quantity[i])
                    for i in range(int(quantity[i])):
                        stock = StockModel()
                        time_data = int(time.time()) + i
                        unique_code = f"{product_get.product_code}-{time_data}"
                        stock.purchase = purchase
                        stock.product = product_get
                        stock.stock_code = unique_code
                        stock.stock_status = 'Active'
                        stock.save()
                purchase_payment = PurchasePaymentModel()
                purchase_payment.purchase = purchase
                purchase_payment.purchase_child = purchase_child
                purchase_payment.total = total
                purchase_payment.pay = pay
                purchase_payment.due = int(total) - int(pay)
                purchase_payment.save()

        return HttpResponse("DataSaved")
    else:
        form = PurchaseForm()
    product_data = ProductTemplate.objects.filter(product_status='Active')
    context = {
        'form': form,
        'product_data': product_data
    }
    return render(request, 'backend/Purchase/purchase.html', context)


@login_required
def purchase_report(request):
    purchase_data = PurchaseChildModel.objects.all()
    context = {
        'purchase_data': purchase_data
    }
    return render(request, 'backend/Purchase/purchase_report.html', context)


@login_required
def product_data_get(request):
    product_id = request.POST.get('product_id')
    product_data = ProductTemplate.objects.filter(pk=product_id)
    value = serializers.serialize('json', product_data)
    return HttpResponse(value, content_type="application/json")
