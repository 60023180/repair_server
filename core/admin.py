from django.contrib import admin
from . import models
from core import models as core_models

# Register your models here.
admin.site.register(core_models.UserProfile)
admin.site.register(core_models.Roles)
admin.site.register(core_models.Permission)
