from django.contrib import admin

from .models import category, color, brand, watchStrap, watchType, clasp, coreMaterial, mainMaterial, Watch

@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug' : ('name',)}

@admin.register(color)
class colorAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug' : ('name',)}

@admin.register(brand)
class brandAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug' : ('name',)}

@admin.register(watchStrap)
class watchStrapAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug' : ('name',)}

@admin.register(watchType)
class watchTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug' : ('name',)}

@admin.register(clasp)
class claspAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug' : ('name',)}

@admin.register(coreMaterial)
class coreMaterialAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug' : ('name',)}

@admin.register(mainMaterial)
class mainMaterialAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug' : ('name',)}

@admin.register(Watch)
class WatchAdmin(admin.ModelAdmin):
    list_display = ['title', 'brand', 'color', 'price', 'slug',
            'in_stock','on_sale', 'is_new', 'is_active', 'created',
            'updated']
    prepopulated_fields = {'slug' : ('title',)}