from django.contrib import admin
from . import models
from core import models as core_models

# Register your models here.
admin.site.register(models.Repair)
admin.site.register(models.GetCategory)
admin.site.register(models.Category)
