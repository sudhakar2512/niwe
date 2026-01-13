

from django.contrib import admin
from .models import Recruitment, RecruitmentDetail, Status, Result, Cancellation, Extension
from django.utils.timezone import now

class RecruitmentDetailInline(admin.TabularInline):
    model = RecruitmentDetail
    extra = 1

class StatusInline(admin.TabularInline):
    model = Status
    extra = 1

class ExtensionInline(admin.TabularInline):
    model = Extension
    extra = 1

class ResultInline(admin.TabularInline):
    model = Result
    extra = 1

class CancellationInline(admin.TabularInline):
    model = Cancellation
    extra = 1

@admin.register(Recruitment)
class RecruitmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_on','is_archived')
    inlines = [RecruitmentDetailInline, StatusInline,ExtensionInline, ResultInline, CancellationInline]
    actions = ['make_archived', 'restore_archived']

    @admin.action(description="Move to Archive")
    def make_archived(self, request, queryset):
        queryset.update(is_archived=True, archived_at=now())

    @admin.action(description="Restore from Archive")
    def restore_archived(self, request, queryset):
        queryset.update(is_archived=False, archived_at=None)

admin.site.register(RecruitmentDetail)
admin.site.register(Status)
admin.site.register(Extension)
admin.site.register(Result)
admin.site.register(Cancellation)
