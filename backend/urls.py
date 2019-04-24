from django.urls import path
from . import views
from . import rbac_views
from . import category_views
from . import sub_category_views
from . import brand_views
from product_template import views as product_template_views
from customer_supplier import views as customer_supplier_views
from pos_section import views as pos_section_views
from purchase import views as purchase_views
from stock import views as stock_views
from reports import views as report_views

urlpatterns = [
    path('', views.backend_home, name="backend_home"),
    path('create_admin', rbac_views.create_admin, name="create_admin"),

    # Category
    path('category', category_views.category, name="category"),
    path('category/status/<int:pk>', category_views.category_status, name="category_status"),
    path('category/delete/<int:pk>', category_views.category_delete, name="category_delete"),
    path('category/edit/<int:pk>', category_views.category_edit, name="category_edit"),
    path('category/pdf', category_views.category_pdf, name="category_pdf"),
    path('category/pdf/download', category_views.category_pdf_download, name="category_pdf_download"),
    path('category/pdf/csv', category_views.export_data_csv, name="export_data_csv"),

    # Sub Category
    path('sub_category', sub_category_views.sub_category, name="sub_category"),
    path('sub_category/delete/<int:pk>', sub_category_views.sub_category_delete, name="sub_category_delete"),
    path('sub_category/status/<int:pk>', sub_category_views.sub_category_status, name="sub_category_status"),
    path('sub_category/edit/<int:pk>', sub_category_views.sub_category_edit, name="sub_category_edit"),
    path('sub_category/pdf', sub_category_views.sub_category_pdf, name="sub_category_pdf"),
    path('sub_category/pdf/download', sub_category_views.sub_category_pdf_download, name="sub_category_pdf_download"),
    path('sub_category/pdf/csv', sub_category_views.sub_export_data_csv, name="sub_export_data_csv"),

    # Brand
    path('brand', brand_views.brand, name="brand"),
    path('brand_report', brand_views.brand_report, name="brand_report"),
    path('brand_report/delete/<int:pk>', brand_views.brand_delete, name="brand_delete"),
    path('brand_report/status/<int:pk>', brand_views.brand_status, name="brand_status"),
    path('brand_report/edit/<int:pk>', brand_views.brand_edit, name="brand_edit"),
    path('brand_report/pdf', brand_views.brand_pdf, name="brand_pdf"),
    path('brand_report/pdf/download', brand_views.brand_pdf_download, name="brand_pdf_download"),
    path('brand_report/csv', brand_views.company_export_data_csv, name="company_export_data_csv"),

    path('product_template', product_template_views.product_template, name="product_template"),
    path('product_template_report', product_template_views.product_template_report, name="product_template_report"),
    path('product_template_report/delete/<int:pk>', product_template_views.product_template_delete,
         name="product_template_delete"),
    path('product_template_report/status/<int:pk>', product_template_views.product_status, name="product_status"),
    path('product_template_report/publish/<int:pk>', product_template_views.product_publish, name="product_publish"),
    path('product_template_report/product_view', product_template_views.product_view, name="product_view"),
    path('product_template_report/get_categories', product_template_views.get_categories, name="get_categories"),
    path('product_template_report/edit/<int:pk>', product_template_views.product_edit, name="product_edit"),

    path('customer', customer_supplier_views.customer, name="customer"),
    path('customer_report', customer_supplier_views.customer_report, name="customer_report"),
    path('customer_report/edit/<int:pk>', customer_supplier_views.customer_edit, name="customer_edit"),
    path('customer_report/delete/<int:pk>', customer_supplier_views.customer_delete, name="customer_delete"),
    path('customer_report/status/<int:pk>', customer_supplier_views.customer_status, name="customer_status"),

    path('supplier', customer_supplier_views.supplier, name="supplier"),
    path('supplier_report', customer_supplier_views.supplier_report, name="supplier_report"),
    path('supplier_report/delete/<int:pk>', customer_supplier_views.supplier_delete, name="supplier_delete"),
    path('supplier_report/status/<int:pk>', customer_supplier_views.supplier_status, name="supplier_status"),
    path('supplier_report/edit/<int:pk>', customer_supplier_views.supplier_edit, name="supplier_edit"),

    path('pos', pos_section_views.pos, name="pos"),
    path('pos/stock_data', pos_section_views.stock_data, name="stock_data"),
    path('pos/add_to_cart', pos_section_views.add_to_cart, name="add_to_cart"),
    path('pos/cart_remove', pos_section_views.cart_remove, name="cart_remove"),
    path('pos/cart_save', pos_section_views.cart_save, name="cart_save"),

    path('stock', stock_views.stock_data, name="stock"),

    path('purchase', purchase_views.purchase, name="purchase"),
    path('purchase/new_pay', purchase_views.new_pay, name="new_pay"),
    path('purchase/report/new_due_payment', purchase_views.new_due_payment, name="new_due_payment"),
    path('purchase/report', purchase_views.purchase_report, name="purchase_report"),
    path('product_data_get', purchase_views.product_data_get, name="product_data_get"),

    path('products_report', report_views.products_report, name="products_report")
]
