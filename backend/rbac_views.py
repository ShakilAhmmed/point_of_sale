from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def create_admin(request):
    return render(request, 'backend/Rbac/create_admin.html')
