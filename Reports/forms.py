from django import forms
from . import models
from .models import State, Prosecution, Reports, Contact_us
from django.forms.widgets import DateInput
from django.utils.translation import gettext as _



attrs = {'class': 'form-control'}
attrss = {'type': 'date', 'class': 'form-control'}






class ReportCreateForm(forms.ModelForm):
    class Meta:
        model = Reports

        fields = '__all__'

        labels = {
            'complainant_name':_('Complainant Name'),
            'complainant_address':_('Complainant Address'),
            'complainant_nationality': _('Complainant Nationality'),
            'complainant_national_number': _('Complainant National Number'),
            'complainant_passport_type': _('Complainant Passport Type'),
            'complainant_passport_number': _('Complainant Passport Number'),
            'complainant_email': _('Complainant Email'),
            'complainant_phone': _('Complainant Phone'),
            'accused_name': _('Accused Name'),
            'report_number': _('Report Number'),
            'state':_('State'),
            'prosecution':_('Prosecution'),
            'police': _('Police'),
            'date_report': _('Date Report'),
            'Materials_of_accusation': _('Materials of Accusation'),
            'summary_report': _('Summary Report'),
            'note': _('Note'),

        }

        widgets = {
            'complainant_name': forms.TextInput(attrs=dict(attrs, placeholder=_('Your Full Name'))),
            'complainant_address': forms.TextInput(attrs=dict(attrs, placeholder=_('Specify Your Address'))),
            'complainant_nationality': forms.Select(attrs=dict(attrss, placeholder=_('What Is Your Nationality'))),
            'complainant_national_number': forms.TextInput(attrs=dict(attrs, placeholder=_('If You are Sudanese, The National Number is Required'))),
            'complainant_passport_type': forms.TextInput(attrs=dict(attrs, placeholder=_('If You are Not Sudanese, The Passport Type is Required'))),
            'complainant_passport_number': forms.TextInput(attrs=dict(attrs, placeholder=_('If You are Not Sudanese, The Passport Number is Required'))),
            'complainant_email': forms.EmailInput(attrs=dict(attrs, placeholder=_('Complainant Email'))),
            'complainant_phone': forms.TextInput(attrs=dict(attrs, placeholder=_('Your Phone or WhatsApp'))),
            'accused_name': forms.TextInput(attrs=dict(attrs, placeholder=_('Accused Full Name'))),
            'report_number': forms.TextInput(attrs=dict(attrs, placeholder=_('Write the report number if you remember it, this helps us'))),
            'police': forms.TextInput(attrs=dict(attrs, placeholder=_('Write the police station where the report was filed'))),
            'date_report': forms.DateInput(attrs=dict(attrss, placeholder=_('Date Report'))),
            'materials_of_accusation': forms.TextInput(attrs=dict(attrs, placeholder=_('Materials of accusation specified by the prosecutor? if you remember it'))),
            'summary_report': forms.TextInput(attrs=dict(attrs, placeholder=_('In less than 300 characters, write a summary of the report, if you remember it'))),
            'note': forms.TextInput(attrs=dict(attrs, placeholder=_('In less than 300 characters, write any notes you want to add'))),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['prosecution'].queryset = Prosecution.objects.none()

        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['prosecution'].queryset = Prosecution.objects.filter(state_id=state_id).order_by('name_arb')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['prosecution'].queryset = self.instance.state.prosecution.order_by('name_arb')

            # Set required fields based on the selected country
        selected_country = self.data.get('complainant_nationality')
        if selected_country == 'SD':  # Sudan's country code is 'SD'
            self.fields['complainant_national_number'].required = True
            self.fields['complainant_passport_type'].required = False
            self.fields['complainant_passport_number'].required = False
        else:
            self.fields['complainant_national_number'].required = False
            self.fields['complainant_passport_type'].required = True
            self.fields['complainant_passport_number'].required = True

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = Contact_us
        fields = '__all__'
        labels = {

            'name':_('Name'),
            'phone': _('Phone'),
            'email': _('Email'),
            'comment': _('Comment'),

        }
        widgets = {
            'name': forms.TextInput(attrs=dict(attrs, placeholder=_('Full Name'))),
            'phone': forms.TextInput(attrs=dict(attrs, placeholder=_('Your phone or WhatsApp'))),
            'email': forms.EmailInput(attrs=dict(attrs, placeholder=_('Your Email'))),
            'comment': forms.TextInput(attrs=dict(attrs, placeholder=_('In less than 300 characters, write Comment'))),
        }