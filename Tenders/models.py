from django.db import models
from tinymce.models import HTMLField
from NiwaProject.settings import alphanumeric
from django.core.validators import FileExtensionValidator
from django.utils.functional import cached_property
import os
from NiwaProject.validation_file import validate_image_file,validate_image_or_pdf_file,validate_pdf_file,validate_file_for_malicious_content,validate_pdf_for_malicious_content,validate_image_metadata_for_malicious_content,validate_image_for_steganography
from NiwaProject.utils import get_file_size, get_file_type_icon_class

# Create your models here.
class TenderPage(models.Model):
    Tender_Title = models.CharField(blank=False, null=False, validators=[alphanumeric])
    # Tender_Pdf = models.FileField(upload_to='tenders/', validators=[validate_pdf_file,validate_file_for_malicious_content])
    Tender_Pdf = models.FileField(upload_to='tenders/', )
    New_Label = models.BooleanField(default=False,blank=True)
    Published_Date = models.DateField(null=True,blank=True)
    Due_Date = models.DateTimeField(null=True,blank=True)
    # Open_Date = models.DateTimeField(null=True,blank=True)

    is_archived = models.BooleanField(default=False, blank=True)
    archived_at = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.Tender_Title    

    def file_size_display(self):
        return get_file_size(self.Tender_Pdf)

    def file_icon_class(self):
        return get_file_type_icon_class(self.Tender_Pdf)[0]
    
    def file_type(self):
        return get_file_type_icon_class(self.Tender_Pdf)[1]
    


class Corrigendum(models.Model):
    tender = models.ForeignKey(TenderPage, related_name='corrigenda', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True,validators=[alphanumeric], help_text="eg: Corrigendum-01")
    # file = models.FileField(upload_to='tenders/', null=True, blank=True,validators=[validate_image_or_pdf_file,validate_file_for_malicious_content])
    file = models.FileField(upload_to='tenders/', null=True, blank=True,)
    New_Label = models.BooleanField(default=False, blank=True)  # NEW field for blinking label

    def __str__(self):
        return self.title or f"Corrigendum for {self.tender.Tender_Title}"
    
    def file_size_display(self):
        return get_file_size(self.file)

    def file_icon_class(self):
        return get_file_type_icon_class(self.file)[0]
    
    def file_type(self):
        return get_file_type_icon_class(self.file)[1]

class PurchaseOrder(models.Model):

    serialNo = models.IntegerField(blank=False)
    title = models.CharField(max_length=255, null=True, blank=False,validators=[alphanumeric], )
    PO_file = models.FileField(upload_to='tenders/purchase_order/', null=True, blank=False,validators=[validate_image_or_pdf_file,validate_file_for_malicious_content])

    is_archived = models.BooleanField(default=False, blank=True)
    archived_at = models.DateTimeField(null=True,blank=True)

    def file_size_display(self):
        return get_file_size(self.PO_file)

    def file_icon_class(self):
        return get_file_type_icon_class(self.PO_file)[0]
    
    def file_type(self):
        return get_file_type_icon_class(self.PO_file)[1]