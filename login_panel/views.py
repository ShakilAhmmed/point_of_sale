from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse
from django.core.mail import send_mail
from django.utils import timezone


# Create your views here.


def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user_data = authenticate(username=username, password=password)
        if user_data is not None:
            #mgs_to_html=render_to_string('email/email.html',{'data':user_data,'time':timezone.now()})
            login(request, user_data)
            messages.success(request, f'Welcome Back {user_data.username}')
            #send_mail(subject, message,sender, [user_data.email],html_message=mgs_to_html,fail_silently=False)
            return HttpResponseRedirect(reverse('backend_home'))
        else:
            messages.error(request, 'Invalid Credentials')
            return HttpResponseRedirect(reverse('admin_login'))
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('backend_home'))
        return render(request, 'login_panel/login.html')


@login_required
def admin_logout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully')
    return HttpResponseRedirect(reverse('admin_login'))
