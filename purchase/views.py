from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from purchase.forms.purchase import PurchaseForm
from .models import PurchaseModel, PurchaseChildModel, PurchasePaymentModel, StockModel
from product_template.models import ProductTemplate
import time
from django.db.models import Sum


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
    purchase_data_grp = PurchaseChildModel.objects.values('purchase').annotate(total=Sum('sub_total'),
                                                                               qty=Sum('quantity'))
    purchase_main_data = PurchaseChildModel.objects.all()
    purchase_payment_data = PurchasePaymentModel.objects.all()
    context = {
        'purchase_data_grp': purchase_data_grp,
        'purchase_main_data': purchase_main_data,
        'purchase_payment_data': purchase_payment_data
    }
    return render(request, 'backend/Purchase/purchase_report.html', context)


@login_required
def product_data_get(request):
    product_id = request.POST.get('product_id')
    product_data = ProductTemplate.objects.filter(pk=product_id)
    value = serializers.serialize('json', product_data)
    return HttpResponse(value, content_type="application/json")


@login_required
def new_pay(request):
    code = request.POST.get('pay_id')
    purchase_payment = PurchasePaymentModel.objects.filter(purchase_id=code)
    value = serializers.serialize('json', purchase_payment)
    return HttpResponse(value, content_type="application/json")


@login_required
def new_due_payment(request):
    #return HttpResponse("ok")

    if request.method == "POST":
        pk = request.POST.get('pk')
        new_pay = request.POST.get('now_pay')
        data = get_object_or_404(PurchasePaymentModel, pk=pk)
        if data:
            data.pay = int(data.pay) + int(new_pay)
            data.due = int(data.due) - int(new_pay)
            data.save()
            return HttpResponse("Updated")
