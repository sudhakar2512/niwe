from django.db import models
from tinymce.models import HTMLField
from NiwaProject.settings import alphanumeric
from NiwaProject.validation_file import validate_forbidden_html_tags

class Certification_Procedure(models.Model):
    title = models.CharField(max_length=250, blank=False, null=False, validators=[alphanumeric])
    description = HTMLField(blank=False,validators=[validate_forbidden_html_tags])
