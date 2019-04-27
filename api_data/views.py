from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from purchase.models import StockModel

# Create your views here.



@api_view()
def get_stock_data(request):
    total_stock = StockModel.objects.filter(stock_status='Active').count()
    if total_stock:
        context = {
            'status': 200,
            'data': total_stock
        }
    else:
        context = {
            'status': 201,
            'data': total_stock
        }
    return Response(context)
@api_view()
def get_purchase_data(request):
    total_purchase = StockModel.objects.all().count()
    if total_purchase:
        context = {
            'status': 200,
            'data': total_purchase
        }
    else:
        context = {
            'status': 201,
            'data': total_purchase
        }
    return Response(context)
@api_view()
def get_sale_data(request):
    total_sale = StockModel.objects.filter(stock_status='Inactive').count()
    if total_sale:
        context = {
            'status': 200,
            'data': total_sale
        }
    else:
        context = {
            'status': 201,
            'data': total_sale
        }
    return Response(context)
