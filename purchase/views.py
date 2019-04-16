from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required
def purchase(request):
    return render(request, 'backend/Purchase/purchase.html')