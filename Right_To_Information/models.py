from tinymce.models import HTMLField
from django.db import models
from django.core.validators import FileExtensionValidator
from NiwaProject.settings import alphanumeric, only_numbers
from NiwaProject.validation_file import validate_forbidden_html_tags, validate_image_file, validate_pdf_file,validate_file_for_malicious_content,validate_pdf_for_malicious_content,validate_image_metadata_for_malicious_content,validate_image_for_steganography
from NiwaProject.utils import get_file_size,get_file_type_icon_class

class RightToInformation(models.Model):

    # title = models.CharField(max_length=255)
    year = models.CharField(max_length=20, null=True, blank=True, validators=[alphanumeric])
    document = models.FileField(upload_to='pdf/', null=True, blank=True, validators=[validate_pdf_file,validate_file_for_malicious_content])

    @property
    def documents_info(self):
        if not self.document:
            return None
        return {
            "size": get_file_size(self.document),
            "icon": get_file_type_icon_class(self.document)[0],
            "type": get_file_type_icon_class(self.document)[1],
        }
  
class Information(models.Model):
    serial = models.IntegerField(default=1)
    title = models.CharField(max_length=250, null=True, blank=True, validators=[alphanumeric])
    document = models.FileField(upload_to='pdf/', null=True, blank=True,validators=[validate_pdf_file,validate_file_for_malicious_content])
    # url=models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class subInformation(models.Model):
    item = models.ForeignKey(Information, on_delete=models.CASCADE)
    description = HTMLField(null=True, blank=True,validators=[validate_forbidden_html_tags])

class AuditReport(models.Model):
    year = models.CharField(max_length=12,unique=True,blank=False, null=True, validators=[alphanumeric])
    pdf_link = models.FileField(upload_to='audit_report/',blank=True,null=True,validators=[validate_pdf_file,validate_file_for_malicious_content])
    description = HTMLField(null=True,blank=True,validators=[validate_forbidden_html_tags])

    def __str__(self):
         return self.year
    
    @property
    def documents_info(self):
        if not self.pdf_link:
            return None
        return {
            "size": get_file_size(self.pdf_link),
            "icon": get_file_type_icon_class(self.pdf_link)[0],
            "type": get_file_type_icon_class(self.pdf_link)[1],
        }
    
    
class AnnualAccount(models.Model):
    year = models.CharField(max_length=12,unique=True,blank=False, null=True, validators=[alphanumeric])
    pdf_link = models.FileField(upload_to='annual_account/',blank=False,null=False, validators=[validate_pdf_file,validate_file_for_malicious_content])    

    def __str__(self):
         return self.year
    
    @property
    def documents_info(self):
        if not self.pdf_link:
            return None
        return {
            "size": get_file_size(self.pdf_link),
            "icon": get_file_type_icon_class(self.pdf_link)[0],
            "type": get_file_type_icon_class(self.pdf_link)[1],
        }
    
class GCminutes(models.Model):
    title = models.CharField(max_length=50,blank=False, null=True, validators=[alphanumeric])
    pdf_link = models.FileField(upload_to='rti/',blank=False,null=True,validators=[validate_pdf_file,validate_file_for_malicious_content])

    class Meta:
        verbose_name = 'GC Minutes'

    def __str__(self):
         return self.title
    
class FinanceReport(models.Model):
    year = models.CharField(max_length=12,unique=True, blank=False, null=True, validators=[alphanumeric])
    pdf_link = models.FileField(upload_to='FinanceReport/',blank=False,null=False , validators=[validate_pdf_file,validate_file_for_malicious_content])
   
    def __str__(self):
         return self.year
    
    @property
    def documents_info(self):
        if not self.pdf_link:
            return None
        return {
            "size": get_file_size(self.pdf_link),
            "icon": get_file_type_icon_class(self.pdf_link)[0],
            "type": get_file_type_icon_class(self.pdf_link)[1],
        }
    
class RTIApplication(models.Model):
    application_year = models.CharField(max_length=12,unique=True,blank=False, null=True, validators=[alphanumeric])
    pdf_link = models.FileField(upload_to='RTI_application/',blank=False,null=False,validators=[validate_pdf_file,validate_file_for_malicious_content])    

    class Meta:
        verbose_name = 'RTI Application'

    def __str__(self):
         return self.application_year
    
    @property
    def documents_info(self):
        if not self.pdf_link:
            return None
        return {
            "size": get_file_size(self.pdf_link),
            "icon": get_file_type_icon_class(self.pdf_link)[0],
            "type": get_file_type_icon_class(self.pdf_link)[1],
        }

class RTI_HOD(models.Model):
    s_no = models.IntegerField()
    Name = models.CharField(max_length=100,blank=False,null=False,validators=[alphanumeric])
    Designation = models.CharField(max_length=100,blank=False,null=True,validators=[alphanumeric])
    From_Date = models.CharField(max_length=50,blank=False,null=True,validators=[alphanumeric])
    To_Date = models.CharField(max_length=50,blank=False,null=True,validators=[alphanumeric])
    Remarks = models.CharField(max_length=100, blank=True,default="",validators=[alphanumeric])  

    class Meta:
        verbose_name = 'RTI Head of Department'
   
    def __str__(self):
        return self.Name
    
class RTI_Tour_type(models.Model):
    type = models.CharField(max_length=15,blank=False,null=True,validators=[alphanumeric])

    class Meta:
        verbose_name = 'RTI Tour type'

    def __str__(self):
        return self.type


class RTI_Tour_details(models.Model):
    item = models.ForeignKey(RTI_Tour_type, on_delete=models.CASCADE)
    year = models.CharField(max_length=50,blank=False,null=True,validators=[alphanumeric])
    pdfLink = models.FileField(upload_to='RTI_Tour/',blank=False, null=True, validators=[validate_pdf_file,validate_file_for_malicious_content])

    def __str__(self):
        return self.item.type

    @property
    def documents_info(self):
        if not self.pdfLink:
            return None
        return {
            "size": get_file_size(self.pdfLink),
            "icon": get_file_type_icon_class(self.pdfLink)[0],
            "type": get_file_type_icon_class(self.pdfLink)[1],
        }
    

class Citizen(models.Model):   
    description = HTMLField(null=True,blank=True,validators=[validate_forbidden_html_tags])

    class Meta:
        verbose_name = 'RTI-Particulars avaliable to Citizen'

class Public_info_Officers(models.Model):   
    description = HTMLField(null=True,blank=True,validators=[validate_forbidden_html_tags])

    class Meta:
        verbose_name = 'RTI-Public Information Officers'

 
    
    