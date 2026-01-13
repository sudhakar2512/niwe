from django.contrib import admin
from .models import *


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):

    list_display = ('title', 'description', 'image_Tag')
    ordering = ['id']


@admin.register(Citizen_Charter)
class Citi_Chart_Admin(admin.ModelAdmin):

    list_display = ('title', 'document_File') 


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):

    list_display = ('id','title', 'document_File', 'url_link')
    ordering = ['id']

    
    # 
class SubGalleryInline(admin.TabularInline):
    model = SubGallery
    extra = 1

class GalleryAdmin(admin.ModelAdmin):
    inlines = [SubGalleryInline]
    list_display=('album_id','title', 'id',)
    
    ordering = ['id']
admin.site.register(Gallery, GalleryAdmin)


class Sub_Think_TankInline(admin.TabularInline):
    model = Sub_Think_Tank
    extra = 1

class Think_TankAdmin(admin.ModelAdmin):
    inlines = [Sub_Think_TankInline]
    list_display=('title', 'id',)
    ordering = ['id']

admin.site.register(Think_Tank, Think_TankAdmin)


class windday2022Admin(admin.ModelAdmin):
    list_display = ('photo')
    search_fields = ('id',)
    list_filter = ('id',)
    ordering = ['id']
admin.site.register(windday_2022)



@admin.register(panindia)
class panindiaAdmin(admin.ModelAdmin):

    list_display = ('image',)
    ordering = ['id']
    search_fields = ('id',)
    list_filter = ('id',)


@admin.register(global_invest)
class global_investAdmin(admin.ModelAdmin):

    list_display = ('image',)
    ordering = ['id']
    search_fields = ('id',)
    list_filter = ('id',)

    
@admin.register(online_training_solar_energy)
class online_training_solar_energyAdmin(admin.ModelAdmin):

    list_display = ('training_photo',)
    ordering = ['id']
    search_fields = ('id',)
    list_filter = ('id',)