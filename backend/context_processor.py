from django.shortcuts import get_object_or_404

from .models import Setup


def settings(request):
    settings_data = get_object_or_404(Setup, pk=1)
    return {'settings': settings_data}
