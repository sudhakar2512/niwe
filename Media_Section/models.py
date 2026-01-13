from django.db import models
from tinymce.models import HTMLField
from django.utils.html import format_html
from django.core.validators import FileExtensionValidator
from NiwaProject.settings import alphanumeric, only_numbers
from NiwaProject.validation_file import validate_forbidden_html_tags, validate_image_file, validate_pdf_file,validate_image_or_pdf_file,validate_file_for_malicious_content,validate_pdf_for_malicious_content,validate_image_metadata_for_malicious_content,validate_image_for_steganography

# awards
class Award(models.Model):
     title = models.CharField(max_length=255, blank=False, null=True,validators=[alphanumeric])
     description = HTMLField(validators=[validate_forbidden_html_tags])
     image_1 = models.ImageField(upload_to='images/', null=True, blank=True,validators=[validate_image_file,validate_file_for_malicious_content])
     image_2 = models.ImageField(upload_to='images/', null=True, blank=True,validators=[validate_image_file,validate_file_for_malicious_content])

     def image_Tag(self): 
          return format_html('<img src="/static/{}" style="width:40px;height:40px;border-radius:50%;" />'.format(self.image_1))
     
     image_Tag.short_description = 'Image'

class Citizen_Charter(models.Model):
     
     title = models.CharField(default="Citizen Charter",blank=False, null=True, validators=[alphanumeric])
     document_File = models.FileField(upload_to='pdf/', max_length=100, validators=[validate_pdf_file,validate_file_for_malicious_content])

# events
class Events(models.Model):

     title = models.CharField(max_length=255, blank=False,null=True,validators=[alphanumeric])
     document_File = models.FileField(upload_to='pdf/', max_length=100, blank=True,null=True,validators=[validate_image_or_pdf_file,validate_file_for_malicious_content])
     url_link = models.URLField(blank=True, null=True, default="Empty")


# for gallery/sub-gallery 


class Gallery(models.Model):
    album_id =   models.IntegerField()
    title = models.CharField(max_length=255, blank=False,null=True,validators=[alphanumeric])
    cover_image = models.ImageField(upload_to='albums/', validators=[validate_image_file,validate_file_for_malicious_content])

    def __str__(self): 
        return self.title

 
class SubGallery(models.Model):
    album = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='subalbums/',validators=[validate_image_file,validate_file_for_malicious_content])

    def __str__(self):
        return f"Sub-Gallery of {self.album.title}"

 
class Think_Tank(models.Model):
    title = models.CharField(max_length=155,blank=False,null=True,validators=[alphanumeric])
#     cover_image = models.ImageField(upload_to='albums/')

    def __str__(self): 
        return self.title

 
class Sub_Think_Tank(models.Model):
    album = models.ForeignKey(Think_Tank, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='subalbums/',validators=[validate_image_file,validate_file_for_malicious_content])

    def __str__(self):
        return f"Sub-Think-tank of {self.album.title}"

class windday_2022(models.Model):
    photo= models.ImageField(upload_to='subalbums/',validators=[validate_image_file,validate_file_for_malicious_content])

class panindia(models.Model):
    image = models.ImageField(upload_to='subalbums/',validators=[validate_image_file,validate_file_for_malicious_content])

class global_invest(models.Model):
    image = models.ImageField(upload_to='subalbums/',validators=[validate_image_file,validate_file_for_malicious_content])

class online_training_solar_energy(models.Model):
  training_photo = models.ImageField(upload_to='subalbums/',validators=[validate_image_file,validate_file_for_malicious_content]) 
