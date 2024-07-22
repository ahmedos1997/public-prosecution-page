from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.Reports)
admin.site.register(models.Prosecution)
admin.site.register(models.State)
admin.site.register(models.Contact_us)

