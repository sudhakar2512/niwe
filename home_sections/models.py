from django.db import models
from tinymce.models import HTMLField
from NiwaProject.settings import alphanumeric,only_numbers
from django.core.validators import FileExtensionValidator
from NiwaProject.validation_file import validate_forbidden_html_tags,validate_image_file,validate_pdf_file, validate_image_or_pdf_file,validate_file_for_malicious_content,validate_pdf_for_malicious_content,validate_image_metadata_for_malicious_content,validate_image_for_steganography
from NiwaProject.utils import get_file_size, get_file_type_icon_class
# Create your models here.



class Related_links(models.Model):
    title = models.CharField(max_length=250, blank=False, null=True, validators=[alphanumeric])
    area=models.CharField(max_length=20, default='India', validators=[alphanumeric])
    description = HTMLField(blank=True,validators=[validate_forbidden_html_tags]) 

class MNRE_WhatsNew(models.Model):
    title = models.CharField(blank=False, validators=[alphanumeric])
    url_link = models.URLField(blank=True)
    Pdf_File = models.FileField(upload_to='MNREWhatsNew/', blank=True, validators=[validate_pdf_file,validate_file_for_malicious_content])
    New_Label = models.BooleanField(default=False)  # NEW field for blinking label
    Published_Date = models.DateField (null=True,blank=True)
    
    is_archived = models.BooleanField(default=False, blank=True)
    archived_at = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.title    

    def file_size_display(self):
        return get_file_size(self.Pdf_File)

    def file_icon_class(self):
        return get_file_type_icon_class(self.Pdf_File)[0]
    
    def file_type(self):
        return get_file_type_icon_class(self.Pdf_File)[1]

    class Meta:
      verbose_name = 'MNRE Whats new'

class Events_New(models.Model):
    title = models.CharField(max_length=255,blank=False, validators=[alphanumeric])
    url_link = models.URLField()
    New_Label = models.BooleanField(default=False)  # NEW field for blinking label

    class Meta:
      verbose_name = 'Events'

# class WhatsNew(models.Model):
#     title = models.CharField(blank=False,null=True, validators=[alphanumeric])
#     url_link = models.URLField(blank=True)   
#     Tender_Pdf = models.FileField(upload_to='WhatsNew/', blank=True, validators=[validate_pdf_file,validate_file_for_malicious_content])
#     New_Label = models.BooleanField(default=False)  # NEW field for blinking label

#     class Meta:
#       verbose_name = 'WhatsNew'

# class WhatsNewCorrigendum(models.Model):
#     tender = models.ForeignKey(WhatsNew, related_name='corrigendam', on_delete=models.CASCADE)
#     title = models.CharField(max_length=255, null=True, blank=False,validators=[alphanumeric])
#     file = models.FileField(upload_to='WhatsNew/', null=True, blank=True,validators=[validate_image_or_pdf_file,validate_file_for_malicious_content])
#     New_Label = models.BooleanField(default=False)  # NEW field for blinking label

#     def __str__(self):
#         return self.title or f"Corrigendum for {self.tender.title}"

class WhatsNew(models.Model):
    title = models.CharField(blank=False,null=True, validators=[alphanumeric])
    url_link = models.URLField(blank=True)   
    # Pdf_File = models.FileField(upload_to='WhatsNew/', blank=True, validators=[validate_pdf_file,validate_file_for_malicious_content])
    Pdf_File = models.FileField(upload_to='WhatsNew/', blank=True, )
    New_Label = models.BooleanField(default=False)  # NEW field for blinking label
    Published_Date = models.DateField (null=True,blank=True)
    
    is_archived = models.BooleanField(default=False, blank=True)
    archived_at = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.title    

    def file_size_display(self):
        return get_file_size(self.Pdf_File)

    def file_icon_class(self):
        return get_file_type_icon_class(self.Pdf_File)[0]
    
    def file_type(self):
        return get_file_type_icon_class(self.Pdf_File)[1]


    class Meta:
      verbose_name = 'WhatsNew'

class WhatsNewCorrigendum(models.Model):
    tender = models.ForeignKey(WhatsNew, related_name='corrigendam', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=False,validators=[alphanumeric])
    # file = models.FileField(upload_to='WhatsNew/', null=True, blank=True,validators=[validate_image_or_pdf_file,validate_file_for_malicious_content])
    file = models.FileField(upload_to='WhatsNew/', null=True, blank=True,)
    New_Label = models.BooleanField(default=False)  # NEW field for blinking label 

    def __str__(self):
        return self.title or f"Corrigendum for {self.tender.title}"
    
    def file_size_display(self):
        return get_file_size(self.file)

    def file_icon_class(self):
        return get_file_type_icon_class(self.file)[0]
    
    def file_type(self):
        return get_file_type_icon_class(self.file)[1]

# class Running_News(models.Model):
#     title = models.CharField(blank=False,null=True, validators=[alphanumeric])
#     url_link = models.URLField()
#     New_Label = models.BooleanField(default=False)  # NEW field for blinking label

#     class Meta:
#       verbose_name = 'Running News'


class Running_News(models.Model):
    title = models.CharField(blank=False,null=True, validators=[alphanumeric])
    url_link = models.URLField(blank=True, null=  True)      
    New_Label = models.BooleanField(default=False)  # NEW field for blinking label

    class Meta:
      verbose_name = 'Running News'

class VisitorCount(models.Model):
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"Total Visitors : {self.count}"
    

class WebsiteLastUpdate(models.Model):
    last_update = models.DateField()

    def __str__(self):
        return f"Last updated: {self.last_update.strftime('%b %d, %Y')}"
