from django.contrib import admin
from about_section.models import AboutUs, DirectorGeneralMessage, Background, charter, OrganizationalChart, QualityPolicy

                                 
# 
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

admin.site.register(AboutUs, AboutAdmin)
# 
class DGMAdmin(admin.ModelAdmin):
    list_display = ('title', 'Dirs_image', 'description')
admin.site.register(DirectorGeneralMessage, DGMAdmin)
# 
class BGAdmin(admin.ModelAdmin):
    list_display = ('description',)
admin.site.register(Background, BGAdmin)
# 
class CharterAdmin(admin.ModelAdmin):
    list_display = ('preamble', 'mission', 'objectives')
admin.site.register(charter, CharterAdmin)
# 
class OrgAdmin(admin.ModelAdmin):
    list_display = ('description', 'image')
admin.site.register(OrganizationalChart, OrgAdmin)
class QualityAdmin(admin.ModelAdmin):
    list_display = ('policyImage',)
admin.site.register(QualityPolicy, QualityAdmin)

