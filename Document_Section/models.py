from django.db import models
from tinymce.models import HTMLField
from NiwaProject.settings import alphanumeric,only_numbers
from django.core.validators import FileExtensionValidator
from NiwaProject.validation_file import validate_forbidden_html_tags,validate_pdf_file,validate_image_file,validate_file_for_malicious_content,validate_pdf_for_malicious_content,validate_image_metadata_for_malicious_content,validate_image_for_steganography
from NiwaProject.utils import get_file_size,get_file_type_icon_class

class Documents(models.Model):

    title = models.CharField(max_length=250, blank=False,null=True, validators=[alphanumeric])
    description = HTMLField(blank=False,validators=[validate_forbidden_html_tags])

    class Meta:
      verbose_name = 'Documents'


# 
class GeneralInformation(models.Model):
    title = models.CharField(max_length=250,blank=False,null=True, validators=[alphanumeric])
    description = HTMLField(blank=True,validators=[validate_forbidden_html_tags]) 

    class Meta:
      verbose_name = 'GeneralInformation'


# 
class ComparisonBetweenFosilFuelAndWind(models.Model):

    heading = models.CharField(max_length=250,blank=False,null=True, validators=[alphanumeric])
    fosil_Fuel = HTMLField(blank=False,validators=[validate_forbidden_html_tags])
    Wind_Energy = HTMLField(blank=False,validators=[validate_forbidden_html_tags])

    class Meta:
      verbose_name = 'Comparison Between Fosil Fuel and Wind'

# 
class RevisedGuidelineForProject(models.Model):
     
    sr_No = models.IntegerField(blank=False)
    title = models.CharField(max_length=512,blank=False,null=True, validators=[alphanumeric])
    documents = models.FileField(upload_to='pdf/',null=True, blank=False,validators=[validate_pdf_file,validate_file_for_malicious_content])
    date = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
      verbose_name = 'Revised Guideline For Project'

    @property
    def documents_info(self):
        return {
            "size": get_file_size(self.documents),
            "icon" : get_file_type_icon_class(self.documents)[0],
            "type": get_file_type_icon_class(self.documents)[1],
        }


class RecordsRetentionSchedule(models.Model):
    ministry_Approval = models.FileField(upload_to='pdf/',null=True, blank=False,validators=[validate_pdf_file,validate_file_for_malicious_content])
    NIEW_Records_Retention_Schedule = models.FileField(upload_to='pdf/',null=True, blank=False,validators=[validate_pdf_file,validate_file_for_malicious_content])

    @property
    def ministry_Approval_info(self):
        return {
            "size": get_file_size(self.ministry_Approval),
            "icon" : get_file_type_icon_class(self.ministry_Approval)[0],
            "type": get_file_type_icon_class(self.ministry_Approval)[1],
        }

    @property
    def NIEW_Records_Retention_Schedule_info(self):
        return {
            "size": get_file_size(self.NIEW_Records_Retention_Schedule),
            "icon" : get_file_type_icon_class(self.NIEW_Records_Retention_Schedule)[0],
            "type": get_file_type_icon_class(self.NIEW_Records_Retention_Schedule)[1],
        }

#


class Newsletters(models.Model):
    issue = models.CharField(max_length=100,blank=False,null=True, validators=[alphanumeric])
    year = models.CharField(max_length=100,blank=False,null=True, validators=[alphanumeric])
    docs_english = models.FileField(upload_to='pdf/',null=True, blank=False,validators=[validate_pdf_file,validate_file_for_malicious_content])
    docs_hindi = models.FileField(upload_to='pdf/',null=True, blank=True,validators=[validate_pdf_file,validate_file_for_malicious_content])
    # docs_english = models.FileField(upload_to='pdf/',null=True, blank=False,)
    # docs_hindi = models.FileField(upload_to='pdf/',null=True, blank=True,)  


    def __str__(self):
        return self.issue
    
    @property
    def docs_english_info(self):
        return {
            "size": get_file_size(self.docs_english),
            "icon" : get_file_type_icon_class(self.docs_english)[0],
            "type": get_file_type_icon_class(self.docs_english)[1],
        }

    @property
    def docs_hindi_info(self):
        return {
            "size": get_file_size(self.docs_hindi),
            "icon" : get_file_type_icon_class(self.docs_hindi)[0],
            "type": get_file_type_icon_class(self.docs_hindi)[1],
        }
        


#    
class AnnualReport(models.Model):
    year = models.CharField(max_length=100,blank=False,null=True, validators=[alphanumeric])
    image = models.ImageField(upload_to='annual-reports/',blank=False,null=True, validators=[validate_image_file,validate_file_for_malicious_content])
    docs_english = models.FileField(upload_to='annual-reports/',blank=False,null=True, validators=[validate_pdf_file,validate_file_for_malicious_content])
    docs_hindi= models.FileField(upload_to='annual-reports/',blank=True,null=True, validators=[validate_pdf_file,validate_file_for_malicious_content])
    # docs_english = models.FileField(upload_to='annual-reports/',blank=False,null=True, )
    # docs_hindi= models.FileField(upload_to='annual-reports/',blank=True,null=True, )

    def __str__(self):
     return f"Annual Report {self.year}"

    @property
    def docs_english_info(self):
        return {
            "size": get_file_size(self.docs_english),
            "icon" : get_file_type_icon_class(self.docs_english)[0],
            "type": get_file_type_icon_class(self.docs_english)[1],
        }

    @property
    def docs_hindi_info(self):
        return {
            "size": get_file_size(self.docs_hindi),
            "icon" : get_file_type_icon_class(self.docs_hindi)[0],
            "type": get_file_type_icon_class(self.docs_hindi)[1],
        }


# class RelatedLinks(models.Model):
#      title = models.CharField(max_length=255,blank=False,null=True, validators=[alphanumeric])
#      linkTitle = HTMLField(blank=False,validators=[validate_forbidden_html_tags])


class FAQs(models.Model):
    preamble = HTMLField(null=True, blank=True,validators=[validate_forbidden_html_tags]) 
    Faq = HTMLField(null=True, blank=True,validators=[validate_forbidden_html_tags]) 

    class Meta:
      verbose_name = 'FAQs'

#  for table year-wise-country


class WEG_Installation_Details_India(models.Model):
    # sr_no = models.IntegerField()
    # state = models.CharField(max_length=100)
    # upto_31_03_2002 = models.DecimalField(max_digits=10, decimal_places=2)
    # year_2002_03 = models.DecimalField(max_digits=10, decimal_places=2)
    # year_2003_04 = models.DecimalField(max_digits=10, decimal_places=2)
    # year_2004_05 = models.DecimalField(max_digits=10, decimal_places=2)
    # year_2005_06 = models.DecimalField(max_digits=10, decimal_places=2)
    # year_2006_07 = models.DecimalField(max_digits=10, decimal_places=2)
    # year_2007_08 = models.DecimalField(max_digits=10, decimal_places=2)
    # year_2008_09 = models.DecimalField(max_digits=10, decimal_places=2)
    # year_2009_10 = models.DecimalField(max_digits=10, decimal_places=2)
    # year_2010_11 = models.DecimalField(max_digits=10, decimal_places=2)
    # year_2011_12 = models.DecimalField(max_digits=10, decimal_places=2)
    # year_2012_13 = models.DecimalField(max_digits=10, decimal_places=2)
    # year_2013_14 = models.DecimalField(max_digits=10, decimal_places=2)
    # year_2014_15 = models.DecimalField(max_digits=10, decimal_places=2)
    # year_2015_16 = models.DecimalField(max_digits=10, decimal_places=2)
    # year_2016_17 = models.DecimalField(max_digits=10, decimal_places=2)
    # year_2017_18 = models.DecimalField(max_digits=10, decimal_places=2)
    # year_2018_19 = models.DecimalField(max_digits=10, decimal_places=2)
    # year_2019_20 = models.DecimalField(max_digits=10, decimal_places=2)
    # year_2020_21 = models.DecimalField(max_digits=10, decimal_places=2)
    # year_2021_22 = models.DecimalField(max_digits=10, decimal_places=2)

    description = HTMLField(null=True, blank=True,validators=[validate_forbidden_html_tags]) 

    class Meta:
        verbose_name = 'WEG Installation Details India'

  


#  for country world-wise
class weg_install_world_wise(models.Model):
    # position = models.IntegerField()
    # country = models.CharField(max_length=100, validators=[alphanumeric])
    # capacity = models.IntegerField()
    description = HTMLField(null=True, blank=True,validators=[validate_forbidden_html_tags]) 

    class Meta:
        verbose_name = 'WEG install World wise'
     
# newslateers.

# class techreports(models.Model):
#     title = models.CharField(max_length=255, blank=False, null=True, validators=[alphanumeric])  # max_length is required
#     description = HTMLField(null=True, blank=True,validators=[validate_forbidden_html_tags]) 

#     class Meta:
#       verbose_name = 'Technical Reports'

class TechnicalReportCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TechnicalReportFile(models.Model):
    category = models.ForeignKey(TechnicalReportCategory, on_delete=models.CASCADE, related_name='files')
    title = models.CharField(max_length=255)
    # file = models.FileField(upload_to='technical_reports/',blank=False,null=True,)
    file = models.FileField(upload_to='technical_reports/',blank=False,null=True, validators=[validate_pdf_file,validate_file_for_malicious_content])
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    @property
    def documents_info(self):
        if not self.file:
            return None
        return {
            "size": get_file_size(self.file),
            "icon": get_file_type_icon_class(self.file)[0],
            "type": get_file_type_icon_class(self.file)[1],
        }


class Library_Sub_Data(models.Model):
    title = models.CharField(max_length=255,blank=False, null=True, validators=[alphanumeric])  # max_length is required
    description = HTMLField(null=True, blank=True,validators=[validate_forbidden_html_tags,validate_file_for_malicious_content]) 


class AKAM_Events_22_23(models.Model):
    title = models.CharField(max_length=255,blank=False,null=True, validators=[alphanumeric])    
    date = models.CharField(max_length=55,blank=False, null=True, validators=[alphanumeric])
    description = HTMLField(blank=False,validators=[validate_forbidden_html_tags])    

    class Meta:
        verbose_name = 'AKAM Events 22-23'

    def __str__(self):
        return self.title

class AKAM_Events_21_22(models.Model):
    title = models.CharField(max_length=255, blank=False,null=True, validators=[alphanumeric])
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)
    Week_no = models.PositiveIntegerField(blank=False, null=True)
    description = HTMLField(blank=False,validators=[validate_forbidden_html_tags])   

    class Meta:
        verbose_name = 'AKAM Events 21-22'

    def __str__(self):
        return self.title
    
