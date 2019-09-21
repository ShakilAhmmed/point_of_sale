from datetime import timezone

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from point_of_sale_project.utils import render_to_pdf

from .models import Category, Company
from .forms.category import CategoryForm
from datetime import date
import csv


@login_required
def category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category Added Successfully')
            return HttpResponseRedirect(reverse('category'))
    else:
        form = CategoryForm()
    category_data = Category.objects.order_by('-id')
    context = {
        'form': form,
        'category_data': category_data,
        'total_data': category_data.count()
    }
    return render(request, 'backend/Category/category.html', context)


@login_required
def category_edit(request, pk):
    category_data = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST or None, instance=category_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category Updated Successfully')
            return HttpResponseRedirect(reverse('category'))
    else:
        form = CategoryForm(instance=category_data)
    context = {
        'form': form
    }
    return render(request, 'backend/Category/category_edit.html', context)


@login_required
def category_status(request, pk):
    category_data = get_object_or_404(Category, pk=pk)
    if category_data.category_status == 'Active':
        category_data.category_status = 'Inactive'
        messages.info(request, 'Category Status Changed Into Inactive')
    else:
        category_data.category_status = 'Active'
        messages.success(request, 'Category Status Changed Into Active')
    category_data.save()
    return HttpResponseRedirect(reverse('category'))


@login_required
def category_delete(request, pk):
    Category.objects.filter(pk=pk).delete()
    messages.warning(request, 'Category Deleted Successfully')
    return HttpResponseRedirect(reverse('category'))


@login_required
def category_pdf(request):
    # return render(request,'backend/Category/category_pdf.html')
    category_data = Category.objects.order_by('-id')
    pdf = render_to_pdf('backend/Category/category_pdf.html', {'category_data': category_data})
    return HttpResponse(pdf, content_type='application/pdf')


@login_required
def category_pdf_download(request):
    # return render(request,'backend/Category/category_pdf.html')
    category_data = Category.objects.order_by('-id')
    pdf = render_to_pdf('backend/Category/category_pdf.html', {'category_data': category_data})
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = f"Category_{date.today()}"
        content = "inline; filename='%s'" % (filename)
        download = request.GET.get("download")
        content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Not found")


@login_required
def export_data_csv(request):
    response = HttpResponse(content_type='text/csv')
    filename = f"Category_{date.today()}"
    response['Content-Disposition'] = f'attachment; filename="{filename}.csv"'

    writer = csv.writer(response)
    writer.writerow(['Category Name', 'Category Code', 'Category Status', 'Created At'])

    category_data = Category.objects.all().values_list('category_name', 'category_code', 'category_status',
                                                       'created_at')
    for category_data_value in category_data:
        writer.writerow(category_data_value)

    return response
