from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from point_of_sale_project.utils import render_to_pdf
from .forms.brand import CompanyForm
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import Company
from datetime import date
import os
import csv


@login_required
def brand(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            if request.POST.get('company_notify'):
                subject = "Congrats!PointOfSale"
                message = 'Congratulations'
                sender = 'no-reply@gmail.com'
                user_email = request.POST.get('company_email')
                mgs_to_html = render_to_string('backend/email/company_email.html')
                send_mail(subject, message, sender,
                          [user_email], html_message=mgs_to_html, fail_silently=False)
            messages.success(request, 'Company Added Successfully')
            return HttpResponseRedirect(reverse('brand'))
    else:
        form = CompanyForm()
    context = {
        'form': form
    }
    return render(request, 'backend/Brand/brand.html', context)


@login_required
def brand_report(request):
    company_data = Company.objects.order_by('-id')
    context = {
        'company_data': company_data
    }
    return render(request, 'backend/Brand/brand_report.html', context)


@login_required
def brand_status(request, pk):
    company_data = get_object_or_404(Company, pk=pk)
    if company_data.company_status == 'Active':
        company_data.company_status = 'Inactive'
        messages.info(request, 'Company Status Changed Into Inactive')
    else:
        company_data.company_status = 'Active'
        messages.success(request, 'Company Status Changed Into Active')
    company_data.save()
    return HttpResponseRedirect(reverse('brand_report'))


@login_required
def brand_edit(request, pk):
    company_data = get_object_or_404(Company, pk=pk)
    old_file = company_data.company_logo
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES, instance=company_data)
        if form.is_valid():
            if request.FILES:
                new_file = request.FILES.get('company_logo')
                if not old_file == new_file:
                    if os.path.isfile(old_file.path):
                        os.remove(old_file.path)
            if request.POST.get('company_notify'):
                subject = "Congrats!PointOfSale"
                message = 'Congratulations'
                sender = 'no-reply@gmail.com'
                user_email = request.POST.get('company_email')
                mgs_to_html = render_to_string('backend/email/company_email.html')
                send_mail(subject, message, sender,
                          [user_email], html_message=mgs_to_html, fail_silently=False)

            form.save()
            messages.success(request, 'Company Updated Successfully')
            return redirect('brand_edit', pk=pk)
    else:
        form = CompanyForm(instance=company_data)
    if company_data.company_logo:
        image = company_data.company_logo.url
    else:
        image = ''
    context = {
        'form': form,
        'image': image
    }
    return render(request, 'backend/Brand/brand_edit.html', context)


@login_required
def brand_delete(request, pk):
    company_data = get_object_or_404(Company, pk=pk)
    if company_data.company_logo:
        if os.path.isfile(company_data.company_logo.path):
            os.remove(company_data.company_logo.path)
    company_data.delete()
    messages.info(request, 'Company Deleted Successfully')
    return HttpResponseRedirect(reverse('brand_report'))


@login_required
def brand_pdf(request):
    brand_data = Company.objects.order_by('-id')
    pdf = render_to_pdf('backend/Brand/brand_pdf.html', {'brand_data': brand_data})
    return HttpResponse(pdf, content_type='application/pdf')


@login_required
def brand_pdf_download(request):
    brand_data = Company.objects.order_by('-id')
    pdf = render_to_pdf('backend/Brand/brand_pdf.html', {'brand_data': brand_data})
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = f"Company_{date.today()}"
        content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Not found")


@login_required
def company_export_data_csv(request):
    response = HttpResponse(content_type='text/csv')
    filename = f"Company_{date.today()}"
    response['Content-Disposition'] = f'attachment; filename="{filename}.csv"'

    writer = csv.writer(response)
    writer.writerow(['Company Name', 'Company Code', 'Company Phone', 'Company Status', 'Created At'])

    company_data = Company.objects.all().values_list('company_name', 'company_code', 'company_phone', 'company_status',
                                                     'created_at')
    for company_data_value in company_data:
        writer.writerow(company_data_value)

    return response
