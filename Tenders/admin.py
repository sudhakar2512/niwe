from django.contrib import admin
from django import forms
from . models import *
from django.utils.timezone import now

class CorrigendumInline(admin.TabularInline):
    model = Corrigendum
    extra = 0  # Number of empty rows for new corrigenda
    fields = ('title', 'file', 'New_Label')  # Fields to display for corrigenda in admin

@admin.register(TenderPage)
class TenderPageAdmin(admin.ModelAdmin):
    search_fields = ('Tender_Title',)
    list_display = ('id','Tender_Title','Published_Date','Due_Date', 'is_archived', 'archived_at', 'New_Label')  # Columns displayed in the TenderPage admin list
    list_filter = ('is_archived', 'New_Label')
    ordering = ['-id']
    inlines = [CorrigendumInline]  # Add the Corrigendum inline to TenderPage admin
    actions = ['make_archived', 'restore_archived']

    @admin.action(description="Move to Archive")
    def make_archived(self, request, queryset):
        queryset.update(is_archived=True, archived_at=now())

    @admin.action(description="Restore from Archive")
    def restore_archived(self, request, queryset):
        queryset.update(is_archived=False, archived_at=None)

# @admin.register(Corrigendum)
# class CorrigendumAdmin(admin.ModelAdmin):
#     list_display = ('title', 'tender', 'New_Label')  # Columns displayed in the Corrigendum admin list
#     list_filter = ('New_Label',)  # Filter by New_Label
#     search_fields = ('title',)  # Search by title


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):

    search_fields = ('PO_file',)
    list_display = ('id','title','PO_file','is_archived', 'archived_at',)
    actions = ['make_archived', 'restore_archived']

    @admin.action(description="Move to Archive")
    def make_archived(self, request, queryset):
        queryset.update(is_archived=True, archived_at=now())

    @admin.action(description="Restore from Archive")
    def restore_archived(self, request, queryset):
        queryset.update(is_archived=False, archived_at=None)


