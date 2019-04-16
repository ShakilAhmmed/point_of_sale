from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import SubCategory
from .forms.sub_category import SubCategoryForm
from django.contrib import messages
from point_of_sale_project.utils import render_to_pdf
from datetime import date
import  csv

@login_required
def sub_category(request):
    sub_category_data = SubCategory.objects.all()
    if request.method == 'POST':
        form = SubCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sub Category Added Successfully')
            return HttpResponseRedirect(reverse('sub_category'))
    else:
        form = SubCategoryForm()
    context = {
        'form': form,
        'sub_category_data': sub_category_data
    }
    return render(request, 'backend/Subcategory/sub_category.html', context)


@login_required
def sub_category_delete(request, pk):
    sub_category_data = get_object_or_404(SubCategory, pk=pk).delete()
    messages.info(request, 'Sub Category Deleted Successfully')
    return HttpResponseRedirect(reverse('sub_category'))


@login_required
def sub_category_status(request, pk):
    sub_category_data = get_object_or_404(SubCategory, pk=pk)
    if sub_category_data.sub_category_status == 'Active':
        sub_category_data.sub_category_status = 'Inactive'
        messages.info(request, 'Status Changed Into Inactive')
    else:
        sub_category_data.sub_category_status = 'Active'
        messages.success(request, 'Status Changed Into Active')
    sub_category_data.save()
    return HttpResponseRedirect(reverse('sub_category'))


@login_required
def sub_category_edit(request, pk):
    sub_category_data = get_object_or_404(SubCategory, pk=pk)
    if request.method == 'POST':
        form = SubCategoryForm(request.POST or None, instance=sub_category_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sub Category Update Successfully')
            return redirect('sub_category_edit', pk=pk)
    else:
        form = SubCategoryForm(instance=sub_category_data)
    context = {
        'form': form
    }
    return render(request, 'backend/Subcategory/edit_sub_category.html', context)


@login_required
def sub_category_pdf(request):
    sub_category_data = SubCategory.objects.order_by('-id')
    pdf = render_to_pdf('backend/Subcategory/sub_category_pdf.html', {'sub_category_data': sub_category_data})
    return HttpResponse(pdf, content_type='application/pdf')


@login_required
def sub_category_pdf_download(request):
    sub_category_data = SubCategory.objects.order_by('-id')
    pdf = render_to_pdf('backend/Subcategory/sub_category_pdf.html', {'sub_category_data': sub_category_data})
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = f"Sub_Category_{date.today()}"
        content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Not found")

@login_required
def sub_export_data_csv(request):
    response = HttpResponse(content_type='text/csv')
    filename = f"Sub_Category_{date.today()}"
    response['Content-Disposition'] = f'attachment; filename="{filename}.csv"'

    writer = csv.writer(response)
    writer.writerow(['Category Name', 'Sub Category Name ','Sub Category Code', 'Sub Category Status', 'Created At'])

    sub_category_data = SubCategory.objects.all().values_list('category_name', 'sub_category_name','sub_category_code', 'sub_category_status',
                                                       'created_at')
    for sub_category_data_value in sub_category_data:
        writer.writerow(sub_category_data_value)

    return response