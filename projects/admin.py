from django.contrib import admin
from django.contrib.contenttypes import generic

from projects.models import CommissionedProject, PersonalProject, Employer, Client, TagCategory, Tag


class TagInlineAdmin(generic.GenericTabularInline):
    model = Tag
    fields = ('name', 'slug', 'category')
    prepopulated_fields = {'slug': ('name',)}


class TaggedProjectAdmin(admin.ModelAdmin):
    inlines = (TagInlineAdmin,)


class TagCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_filter = ('category',)


admin.site.register(Client)
admin.site.register(Employer)
admin.site.register(CommissionedProject, TaggedProjectAdmin)
admin.site.register(PersonalProject, TaggedProjectAdmin)
admin.site.register(TagCategory, TagCategoryAdmin)
admin.site.register(Tag, TagAdmin)