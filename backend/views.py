from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
@login_required
def backend_home(request):
    return render(request, 'backend/home.html')








