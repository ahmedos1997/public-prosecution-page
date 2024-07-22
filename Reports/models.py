from django.db import models
from django_countries.fields import CountryField
import random
from django.utils.translation import gettext_lazy as _

class State(models.Model):
    name_arb = models.CharField(max_length=255)
    name_eng = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name_arb


class Prosecution(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name_arb = models.CharField(max_length=255)
    name_eng = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name_arb


class Reports(models.Model):
    follow_number = models.BigIntegerField(unique=True, editable=False)
    complainant_name = models.CharField(max_length=255)
    complainant_address = models.CharField(max_length=255)
    complainant_nationality = models.CharField(max_length=200,  null=True, choices=CountryField().choices + [('', _('Select Country'))])
    complainant_national_number = models.DecimalField(max_digits=11, decimal_places=0, null=True, blank=True)
    complainant_passport_type = models.CharField(max_length=50, null=True, blank=True)
    complainant_passport_number = models.CharField(max_length=255, null=True, blank=True)
    complainant_email = models.EmailField(null=True, blank=True)
    complainant_phone = models.DecimalField(max_digits=20, decimal_places=0, null=True, blank=True)
    accused_name = models.CharField(max_length=255)
    report_number = models.CharField(max_length=255, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING)
    prosecution = models.ForeignKey(Prosecution, on_delete=models.PROTECT, default=None)
    police = models.CharField(max_length=255, null=True, blank=True)
    date_report = models.DateField(null=True, blank=True, default=None)
    materials_of_accusation = models.CharField(max_length=255, null=True, blank=True)
    summary_report = models.TextField(max_length=300)
    note = models.TextField(max_length=300, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.follow_number:
            self.follow_number = random.randint(10000, 99999)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.complainant_name

class Contact_us(models.Model):
    follow_number = models.BigIntegerField(unique=True, editable=False)
    name = models.CharField(max_length=255)
    phone = models.DecimalField(max_digits=20, decimal_places=0, null=False)
    email = models.EmailField(null=True, blank=True)
    comment = models.CharField(max_length=300, null=False)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.follow_number:
            self.follow_number = random.randint(10000, 99999)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name