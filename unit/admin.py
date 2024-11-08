from django.contrib import admin
from .models import Stand, Smokehouse, Hosper, Image

class ImageInline(admin.TabularInline):
    model = Image
    extra = 4

@admin.register(Stand)
class StandAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ('model', 'price', 'availability')
    search_fields = ('model',)

@admin.register(Smokehouse)
class SmokehouseAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ('model', 'price', 'availability')
    search_fields = ('model',)

@admin.register(Hosper)
class HosperAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ('model', 'price', 'availability')
    search_fields = ('model',)