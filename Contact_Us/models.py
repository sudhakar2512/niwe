from django.db import models
from tinymce.models import HTMLField
from NiwaProject.validation_file import validate_forbidden_html_tags

class ContactUs(models.Model):

    feedback_and_Address = HTMLField(blank=False, validators=[validate_forbidden_html_tags])
    testing_and_Research_Station = HTMLField(blank=False, validators=[validate_forbidden_html_tags])
    
    class Meta:
        verbose_name = "Contact US"