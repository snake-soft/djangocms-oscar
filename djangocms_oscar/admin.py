from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from .models import MyModel


class PlaceholderAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass

admin.site.register(MyModel, PlaceholderAdmin)
