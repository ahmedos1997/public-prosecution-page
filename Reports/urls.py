from django.contrib import admin
from django.urls import path , include

from . import views
urlpatterns = [
    path('report_create', views.report_create, name='report_create'),
    path('success/<int:follow_number>/', views.Success, name='success'),
    path('ajax/load-prosecution/', views.load_prosecution, name='ajax_load_prosecution'),     # يجب عمل url للدالة الخاصة بالنيابات
    path('report_view/<int:id>', views.report_view, name='report_view'),
    path('report_list', views.report_list, name='report_list'),
    path('get_queryset/', views.get_queryset, name='get_queryset'),
    path('report_print/<int:id>', views.report_print, name='report_print'),
    path('contact_us_create', views.contact_us_create, name='contact_us_create'),
    path('contact_us_list', views.contact_us_list, name='contact_us_list'),
    path('contact_us_view/<int:id>', views.contact_us_view, name='contact_us_view'),
]