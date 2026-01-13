from django.db import models
from tinymce.models import HTMLField
from NiwaProject.settings import alphanumeric
from NiwaProject.validation_file import validate_forbidden_html_tags, validate_image_file,validate_file_for_malicious_content,validate_pdf_for_malicious_content,validate_image_metadata_for_malicious_content,validate_image_for_steganography
from django.core.validators import FileExtensionValidator


# 
class AboutUs(models.Model):
    title = models.CharField(max_length=255,blank=False, null=False, validators=[alphanumeric] )
    description = HTMLField(blank=False, validators=[validate_forbidden_html_tags])
# 
class DirectorGeneralMessage(models.Model):
    title = models.CharField(max_length=255,blank=False, null=False, validators=[alphanumeric])
    Dirs_image = models.ImageField(upload_to="images/", null=True, default=None, validators=[validate_image_file,validate_file_for_malicious_content])
    description = HTMLField(validators=[validate_forbidden_html_tags]) 
# 
class Background(models.Model):
    description = HTMLField(blank=False,validators=[validate_forbidden_html_tags])   
# 
class charter(models.Model):
    preamble = HTMLField(blank=False,validators=[validate_forbidden_html_tags])
    mission = HTMLField(blank=False,validators=[validate_forbidden_html_tags])
    objectives = HTMLField(blank=False,validators=[validate_forbidden_html_tags])
    # 
class OrganizationalChart(models.Model):
    description = HTMLField(validators=[validate_forbidden_html_tags])
    image = models.ImageField(upload_to='images/', null=True, default=None,validators=[validate_image_file,validate_file_for_malicious_content])
# 
class QualityPolicy(models.Model):
    policyImage =  models.ImageField(upload_to='images/', null=True, default=None,validators=[validate_image_file,validate_file_for_malicious_content])


