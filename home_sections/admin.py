from django.contrib import admin
from . models import *
from django.utils.timezone import now

# Register your models here.

@admin.register(Related_links)
class RelatedLinksAdmin(admin.ModelAdmin):

    list_display = ('id','title', 'description')
    ordering = ['id']

@admin.register(MNRE_WhatsNew)
class MNRE_WhatsNewAdmin(admin.ModelAdmin):
    list_display = ('id','title','Published_Date','New_Label', 'is_archived')
    ordering = ['id']

    actions = ['make_archived', 'restore_archived']

    @admin.action(description="Move to Archive")
    def make_archived(self, request, queryset):
        queryset.update(is_archived=True, archived_at=now())

    @admin.action(description="Restore from Archive")
    def restore_archived(self, request, queryset):
        queryset.update(is_archived=False, archived_at=None)


@admin.register(Events_New)
class Events_NewAdmin(admin.ModelAdmin):
    list_display = ("title",'url_link','New_Label')
    ordering = ['id']

class CorrigendumInline(admin.TabularInline):
    model = WhatsNewCorrigendum
    extra = 0  # Number of empty rows for new corrigenda
    fields = ('title', 'file', 'New_Label')  # Fields to display for corrigenda in admin

@admin.register(WhatsNew)
class WhatsNewAdmin(admin.ModelAdmin):
    list_display = ("title",'url_link','New_Label','Published_Date')
    ordering = ['-id']
    inlines = [CorrigendumInline]

    actions = ['make_archived', 'restore_archived']

    @admin.action(description="Move to Archive")
    def make_archived(self, request, queryset):
        queryset.update(is_archived=True, archived_at=now())

    @admin.action(description="Restore from Archive")
    def restore_archived(self, request, queryset):
        queryset.update(is_archived=False, archived_at=None)

@admin.register(Running_News)
class Running_NewsAdmin(admin.ModelAdmin):
    list_display = ('id',"title",'url_link','New_Label')
    ordering = ['id']

        
@admin.register (VisitorCount)
class VisitorCountAdmin(admin.ModelAdmin):
    list_display = ('count',)

@admin.register (WebsiteLastUpdate)
class WebsiteLastUpdateAdmin(admin.ModelAdmin):
    list_display = ('last_update',)