from django.urls import path
from . import views
urlpatterns=[
    path('',views.admin_login,name="admin_login"),
    path('admin_logout', views.admin_logout, name="admin_logout"),
]