from django.contrib import admin

# Register your models here.
from . import models
admin.site.register(models.usercomments)
admin.site.register(models.userinformation)
admin.site.register(models.products)
