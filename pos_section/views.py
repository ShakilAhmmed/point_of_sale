from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core import serializers
from product_template.models import ProductTemplate
from django.db.models import Q

# Create your views here.
from purchase.models import StockModel

from customer_supplier.models import CustomerModel
from .cart import Cart


@login_required
def pos(request):
    customer = CustomerModel.objects.filter(customer_status='Active')
    products = ProductTemplate.objects.filter(product_status='Active', is_published=True)
    if request.method == "GET" and request.GET.get('search'):
        search_key = request.GET.get('search')
        if search_key.isnumeric():
            # products = ProductTemplate.objects.filter(Q(product_mrp__lte=search_key) | Q(product_tax__lte=search_key))
            products = ProductTemplate.objects.filter(product_code__contains=search_key, product_status='Active',
                                                      is_published=True)
        else:
            products = ProductTemplate.objects.filter(product_name__contains=search_key, product_status='Active',
                                                      is_published=True)

    context = {
        'customer': customer,
        'products': products,
        'values': request.GET,
    }
    return render(request, 'backend/POS/pos.html', context)


@login_required
def stock_data(request):
    product_id = request.POST.get('product_id')
    stock_data = StockModel.objects.filter(product_id=product_id, stock_status='Active').count()
    return HttpResponse(stock_data, content_type="application/json")


@login_required
def add_to_cart(request):
    cart = Cart(request)
    product_id = request.POST.get('add_to_cart_product_id', None)
    products = get_object_or_404(ProductTemplate, pk=product_id)
    quantity = request.POST.get('quantity', None)
    update_quantity = request.POST.get('update_quantity', None)

    if products and quantity is not None:
        data = cart.add(product=products, quantity=int(quantity))
        return HttpResponse("Added")
    elif update_quantity is not None:
        data = cart.add(product=products, quantity=int(update_quantity), update_quantity=int(update_quantity))
        return HttpResponse("Updated")
    # return HttpResponse(update_quantity)
    # cart_data = {}
    # cart_data['product_id'] = add_to_cart_product_id
    # cart_data['quantity'] = quantity
    # session_products_details = []
    # previous_session_data = request.session.get('products_details', None)
    # if previous_session_data is None:
    #     session_products_details = request.session['products_details'] = []
    #     session_products_details.append(cart_data)
    # else:
    #     for i in previous_session_data:
    #         if add_to_cart_product_id == i.get('product_id'):
    #             new_quantity= int(i.get('quantity')) + int(quantity)
    #             i.update({'product_id':add_to_cart_product_id,'quantity':str(new_quantity)})
    #     previous_session_data.append(cart_data)
    #     request.session['products_details'] = previous_session_data
    # print("If None", session_products_details)
    # print("If Not None", previous_session_data)


@login_required
def cart_remove(request):
    cart = Cart(request)
    product_id = request.POST.get('product_id', None)
    if product_id is not None:
        product = get_object_or_404(ProductTemplate, id=product_id)
        cart.remove(product)
        return HttpResponse("Deleted")
