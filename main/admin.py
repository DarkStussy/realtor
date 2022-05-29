from django.contrib import admin
from .models import Estate, Realtor, EstateImages

admin.site.register(Realtor)


class ImagesInline(admin.TabularInline):
    model = EstateImages
    raw_id_fields = ['estate']


@admin.register(Estate)
class EstateAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'area', 'price']
    list_filter = ['realtor', 'area', 'price']
    inlines = [ImagesInline]
