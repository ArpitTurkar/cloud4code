from django.contrib import admin

from .models import User

# Register your models here.
# class useradmin(admin.ModelAdmin):
#     list_display=['email']
admin.site.register(User)
