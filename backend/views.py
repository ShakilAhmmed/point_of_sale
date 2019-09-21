from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from backend.models import Setup
import os

# Create your views here.
from backend.forms.setup import SetupForm


@login_required
def backend_home(request):
    return render(request, 'backend/home.html')


@login_required
def setup(request, pk):
    settings_data = get_object_or_404(Setup, pk=pk)
    old_file = settings_data.company_logo
    if request.method == "POST":
        form = SetupForm(request.POST, request.FILES, instance=settings_data)
        if form.is_valid():
            if request.FILES:
                new_file = request.FILES.get('company_logo')
                if not old_file == new_file:
                    if os.path.isfile(old_file.path):
                        os.remove(old_file.path)
            form.save()
            messages.success(request, 'Settings Updated Successfully')
            return redirect('setup', pk=pk)
    else:
        form = SetupForm(instance=settings_data)
    if old_file:
        image = old_file.url
    else:
        image = ''
    context = {
        'form': form,
        'settings_data': settings_data,
        'image': image
    }

    return render(request, 'backend/Settings/setup.html', context)
