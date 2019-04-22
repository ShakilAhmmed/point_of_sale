from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse

from .forms.product_template import ProductTemplateForm, ProductTemplateCategoryForm
from backend.models import Category, SubCategory

from .models import ProductTemplate, ProductTemplateCategory, ProductTemplateSubCategory, ProductTemplateImages
import os


@login_required
def product_template(request):
    if request.method == 'POST':
        form = ProductTemplateForm(request.POST, request.FILES)
        if form.is_valid():
            new_data = form.save()
            product_category = request.POST.getlist('product_category[]')
            product_sub_category = request.POST.getlist('product_sub_category[]')
            product_image_title = request.POST.getlist('product_image_title[]', None)
            product_image_data = request.FILES.getlist('product_image_data[]', None)
            for product_category_data in product_category:
                category_data = get_object_or_404(Category, pk=product_category_data)
                category = ProductTemplateCategory()
                category.product_template_id = new_data.pk
                category.product_category = category_data
                category.save()
            for product_sub_category_data in product_sub_category:
                sub_category = ProductTemplateSubCategory()
                sub_category_data = get_object_or_404(SubCategory, pk=product_sub_category_data)
                sub_category.product_template_id = new_data.pk
                sub_category.product_sub_category = sub_category_data
                sub_category.save()
            if product_image_data and product_image_title:
                for i in range(len(product_image_title)):
                    other_images = ProductTemplateImages()
                    other_images.product_template = new_data
                    other_images.product_image_title = product_image_title[i]
                    other_images.product_image = product_image_data[i]
                    other_images.save()
            messages.success(request, 'New Product Template Created Successfully')
            return HttpResponseRedirect(reverse('product_template'))

    else:
        form = ProductTemplateForm()
    category = Category.objects.filter(category_status='Active')
    sub_category = SubCategory.objects.filter(sub_category_status='Active')
    context = {
        'form': form,
        'category': category,
        'sub_category': sub_category
    }
    return render(request, 'backend/Product/product_template.html', context)


@login_required
def product_template_report(request):
    product_template = ProductTemplate.objects.order_by('-id')
    context = {
        'product_template': product_template
    }
    return render(request, 'backend/Product/product_template_report.html', context)


@login_required
def product_status(request, pk):
    product_template_data = get_object_or_404(ProductTemplate, pk=pk)
    if product_template_data.product_status == 'Active':
        product_template_data.product_status = 'Inactive'
        messages.info(request, 'Status Changed Into Inactive')
    else:
        product_template_data.product_status = 'Active'
        messages.success(request, 'Status Changed Into Active')
    product_template_data.save()
    return HttpResponseRedirect(reverse('product_template_report'))


@login_required
def product_publish(request, pk):
    product_template_data = get_object_or_404(ProductTemplate, pk=pk)
    print(product_template_data.is_published)
    if product_template_data.is_published:
        messages.warning(request, 'Drafted')
        product_template_data.is_published = False
    else:
        product_template_data.is_published = True
        messages.success(request, 'Published')
    product_template_data.save()
    return HttpResponseRedirect(reverse('product_template_report'))


@login_required
def product_edit(request, pk):
    product_template_data = get_object_or_404(ProductTemplate, pk=pk)
    old_file = product_template_data.cover_image
    if request.method == "POST":
        form = ProductTemplateForm(request.POST, request.FILES, instance=product_template_data)
        if form.is_valid():
            if request.FILES:
                new_file = request.FILES.get('cover_image')
                if not old_file == new_file:
                    if os.path.isfile(old_file.path):
                        os.remove(old_file.path)
            new_data = form.save()
            product_category_update = request.POST.getlist('product_category[]')
            product_sub_category_update = request.POST.getlist('product_sub_category[]')
            prev_category = ProductTemplateCategory.objects.filter(product_template_id=pk).delete()
            for product_category_data in product_category_update:
                category_data_get = get_object_or_404(Category, pk=product_category_data)
                category = ProductTemplateCategory()
                category.product_template_id = new_data.pk
                category.product_category = category_data_get
                category.save()
            prev_category = ProductTemplateSubCategory.objects.filter(product_template_id=pk).delete()
            for product_sub_category_data in product_sub_category_update:
                sub_category = ProductTemplateSubCategory()
                sub_category_data = get_object_or_404(SubCategory, pk=product_sub_category_data)
                sub_category.product_template_id = new_data.pk
                sub_category.product_sub_category = sub_category_data
                sub_category.save()
            messages.success(request, 'Product Updated Successfully')
            return redirect('product_edit', pk=pk)
    else:
        form = ProductTemplateForm(instance=product_template_data)
    product_category = ProductTemplateCategory.objects.filter(product_template_id=pk)
    category = Category.objects.filter(category_status='Active')
    product_sub_category = ProductTemplateSubCategory.objects.filter(product_template_id=pk)
    sub_category = SubCategory.objects.filter(sub_category_status='Active')
    product_other_images = ProductTemplateImages.objects.filter(product_template_id=pk)
    if product_template_data.cover_image:
        image = product_template_data.cover_image.url
    else:
        image = ''

    context = {
        'form': form,
        'category': category,
        'sub_category': sub_category,
        'product_category': product_category,
        'product_sub_category': product_sub_category,
        'image': image,
        'product_other_images': product_other_images
    }
    return render(request, 'backend/Product/product_template_edit.html', context)


@login_required
def product_view(request):
    code = request.POST.get("code")
    # context = {
    #     'product_template_data': ProductTemplate.objects.filter(product_code=code)
    # }
    # return JsonResponse(context)
    product_template_data = ProductTemplate.objects.filter(product_code=code)
    value = serializers.serialize('json', product_template_data)
    return HttpResponse(value, content_type="application/json")


@login_required
def get_categories(request):
    product_id = request.POST.get("product_id")
    product_template_category_data = ProductTemplateCategory.objects.get(product_template_id=product_id)
    value = serializers.serialize('json', product_template_category_data)
    return HttpResponse(value, content_type="application/json")


@login_required
def product_template_delete(request, pk):
    product_template_data = get_object_or_404(ProductTemplate, pk=pk)
    if product_template_data.cover_image:
        if os.path.isfile(product_template_data.cover_image.path):
            os.remove(product_template_data.cover_image.path)

    other_images = ProductTemplateImages.objects.filter(product_template_id=pk)
    for other_images_data in other_images:
        if other_images_data.product_image:
            if os.path.isfile(other_images_data.product_image.path):
                os.remove(other_images_data.product_image.path)
    other_images.delete()
    product_template_data.delete()

    messages.info(request, 'Product Template Deleted Successfully')
    return HttpResponseRedirect(reverse('product_template_report'))
