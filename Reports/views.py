from datetime import datetime

from django.shortcuts import render , redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from . import models, forms
from .models import Reports, State, Prosecution, Contact_us
from .forms import  ReportCreateForm, ContactUsForm
from django.db.models import Q
from django.core.paginator import Paginator

from django.core.exceptions import ValidationError


# Create your views here.

#################################### report  #########################################


def report_create(request):
    if request.method == 'POST':
        form = ReportCreateForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.save()
            follow_number = report.follow_number
            return redirect('success', follow_number=follow_number)
    else:
        form = ReportCreateForm()
    return render(request, 'page/report_create.html', {'form': form, 'follow_number': None})

def load_prosecution(request):
    state_id = request.GET.get('state')
    prosecutions = Prosecution.objects.filter(state_id=state_id).order_by('name_arb')
    return render(request, 'page/prosecution_option.html', {'prosecutions': prosecutions})

def Success(request, follow_number):
    return render(request, 'page/success.html', {'follow_number':follow_number})





def report_list(request):

    reports = Reports.objects.order_by('-date_report')
    total_report = Reports.objects.all().count()
    paginate_by = 10


    paginator = Paginator(reports, paginate_by)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'reports': page_obj,
        'total_report': total_report,
        'paginate_by': paginate_by,
        'page_obj': page_obj  # تمرير كائن الصفحة إلى السياق
    }
    return render(request, 'page/report_list.html', context)

 # عملية البحث
def get_queryset(request):
    query = request.GET.get('q')
    reports = Reports.objects.filter(
        Q(follow_number__icontains=query) |
        Q(complainant_name__icontains=query) |
        Q(complainant_passport_number=query) |
        Q(accused_name__icontains=query) |
        Q(report_number__icontains=query)|
        Q(state__name_arb__icontains=query)|
        Q(prosecution__name_arb__icontains=query)
    )
    total_report = reports.count()
    context = {
        'reports':reports,
        'total_report':total_report
    }
    return render(request, 'page/report_list.html', context)


def report_view(request, id):
    report = Reports.objects.get(id=id)
    report.date_report = report.date_report.strftime('%d-%m-%Y')
    context = {
        'report':report,
    }
    return render(request, 'page/report_view.html', context)

def report_print(request, id):
    report = Reports.objects.get(id=id)
    report.date_report = report.date_report.strftime('%d-%m-%Y')
    context = {
        'report':report,
    }
    return render(request, 'page/report_print.html', context)

#################################### contact us  #########################################

def contact_us_create(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            contact_us = form.save(commit=False)
            contact_us.save()
            follow_number = contact_us.follow_number
            return redirect('success', follow_number=follow_number)
    else:
        form = ContactUsForm
    return render(request, 'page/contact_us_create.html', {'form' : form, 'follow_number': None})



def contact_us_list(request):
    contact_us = Contact_us.objects.order_by('-date')

    context = {
        'contact_us':contact_us
    }
    return render(request, 'page/contact_us_list.html', context)


def contact_us_view(request, id):
    contact_us = Contact_us.objects.get(id=id)
    context = {
        'contact_us':contact_us
    }
    return render(request, 'page/contact_us_view.html', context)