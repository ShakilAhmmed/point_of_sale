from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from purchase.forms.purchase import PurchaseForm

from product_template.models import ProductTemplate


@login_required
def purchase(request):
    form = PurchaseForm()
    product_data = ProductTemplate.objects.filter(product_status='Active')
    context = {
        'form': form,
        'product_data': product_data
    }
    return render(request, 'backend/Purchase/purchase.html', context)

@login_required
def product_data_get(request):
    product_id=request.POST.get('product_id')
    product_data=ProductTemplate.objects.filter(pk=product_id)
    value = serializers.serialize('json', product_data)
    return HttpResponse(value, content_type="application/json")
