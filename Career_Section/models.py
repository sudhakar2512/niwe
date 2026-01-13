from django.db import models
from tinymce.models import HTMLField
from NiwaProject.validation_file import validate_forbidden_html_tags, validate_image_file,validate_file_for_malicious_content,validate_pdf_for_malicious_content,validate_image_metadata_for_malicious_content,validate_image_for_steganography
from NiwaProject.utils import get_file_size,get_file_type_icon_class

class Recruitment(models.Model):
    title = models.CharField(max_length=200)
    notification = models.FileField(upload_to='pdf/', null=True, blank=True)
    published_on = models.DateField(null=True, blank=True)
    New_Label = models.BooleanField(default=False,blank=True)
    is_archived = models.BooleanField(default=False, blank=True)
    archived_at = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.title
    
    @property
    def documents_info(self):
        return {
            "size": get_file_size(self.notification),
            "icon" : get_file_type_icon_class(self.notification)[0],
            "type": get_file_type_icon_class(self.notification)[1],
        }


class RecruitmentDetail(models.Model):
    recruitment = models.ForeignKey(Recruitment, on_delete=models.CASCADE, related_name='job_posts')
    sr_no = models.IntegerField()
    name_of_post = models.CharField(max_length=256)
    application_form = models.FileField(upload_to='pdf/', null=True, blank=True)    
    New_Label = models.BooleanField(default=False,blank=True)

    def __str__(self):
        return self.name_of_post
    
    @property
    def documents_info(self):
        return {
            "size": get_file_size(self.application_form),
            "icon" : get_file_type_icon_class(self.application_form)[0],
            "type": get_file_type_icon_class(self.application_form)[1],
        }



class Status(models.Model):
    recruitment = models.ForeignKey(Recruitment, on_delete=models.CASCADE, related_name='statuses')
    title = models.CharField(max_length=256)
    file = models.FileField(upload_to='pdf/', null=True, blank=True)
    New_Label = models.BooleanField(default=False,blank=True)

    def __str__(self):
        return f"{self.recruitment.title} - {self.title}"
    
    @property
    def documents_info(self):
        return {
            "size": get_file_size(self.file),
            "icon" : get_file_type_icon_class(self.file)[0],
            "type": get_file_type_icon_class(self.file)[1],
        }

    
class Extension(models.Model):

    recruitment = models.ForeignKey(Recruitment, on_delete=models.CASCADE, related_name='extensions')
    title = models.CharField(max_length=256)
    file = models.FileField(upload_to='pdf/', null=True, blank=True)
    New_Label = models.BooleanField(default=False,blank=True)

    def __str__(self):
        return f"{self.recruitment.title} - {self.title}"
    
    @property
    def documents_info(self):
        return {
            "size": get_file_size(self.file),
            "icon" : get_file_type_icon_class(self.file)[0],
            "type": get_file_type_icon_class(self.file)[1],
        }

class Result(models.Model):
    recruitment = models.ForeignKey(Recruitment, on_delete=models.CASCADE, related_name='results')
    description = models.CharField(max_length=256, null=True, blank=True)
    file = models.FileField(upload_to='pdf/', null=True, blank=True)
    New_Label = models.BooleanField(default=False,blank=True)

    def __str__(self):
        return f"{self.recruitment.title} - Result"
    
    @property
    def documents_info(self):
        return {
            "size": get_file_size(self.file),
            "icon" : get_file_type_icon_class(self.file)[0],
            "type": get_file_type_icon_class(self.file)[1],
        }


class Cancellation(models.Model):
    recruitment = models.ForeignKey(Recruitment, on_delete=models.CASCADE, related_name='cancellations')
    title = models.CharField(max_length=256)
    file = models.FileField(upload_to='pdf/')
    New_Label = models.BooleanField(default=False,blank=True)
    def __str__(self):
        return f"{self.recruitment.title} - Cancelled"
    
    @property
    def documents_info(self):
        return {
            "size": get_file_size(self.file),
            "icon" : get_file_type_icon_class(self.file)[0],
            "type": get_file_type_icon_class(self.file)[1],
        }
