from django.contrib import admin
from models import Taxonomy


class TaxonomyAdmin(admin.ModelAdmin):
    list_display = ('key', 'val')
    search_fields = ('key',)



admin.site.register(Taxonomy, TaxonomyAdmin)