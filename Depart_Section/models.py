from django.db import models
from tinymce.models import HTMLField
from django.utils.text import slugify
from NiwaProject.settings import alphanumeric, only_numbers
from django.core.validators import FileExtensionValidator
from NiwaProject.validation_file import validate_forbidden_html_tags, validate_image_file, validate_pdf_file,validate_file_for_malicious_content,validate_filename



# Create your models here.\

# departments
class Departments(models.Model):
    title = models.CharField(max_length=255,blank=False,validators=[alphanumeric])
    description = HTMLField(blank=False,validators=[validate_forbidden_html_tags])

    class Meta:
      verbose_name = 'Departments'


# research 
class Reserach_n_Development(models.Model):
    title = models.CharField(max_length=255, validators=[alphanumeric],blank=False,null=True)
    description = HTMLField(null=True, blank=True,validators=[validate_forbidden_html_tags])
    # document_File = models.FileField(upload_to='pdf/', null=True, blank=True,validators=[validate_pdf_file])

    class Meta:
      verbose_name = 'Reserach and Development'


# SNR_menu
class Testing_and_Standards_Regulation(models.Model):
    title = models.CharField(max_length=255, validators=[alphanumeric],blank=False,null=True)  # max_length is required
    description = HTMLField(null=True, blank=True,validators=[validate_forbidden_html_tags])
    # document_File = models.FileField(upload_to="pdf/", null=True, blank=True)

    class Meta:
      verbose_name = 'Testing and Standards & Regulation'

 # testing_menu
class Testing_menu(models.Model):
    title = models.CharField(max_length=255, validators=[alphanumeric],blank=False,null=True)  # max_length is required
    description = HTMLField(null=True, blank=True,validators=[validate_forbidden_html_tags])

    class Meta:
      verbose_name = 'Testing menu'
    

class Wind_Terbine_photo(models.Model):
    terbine_photo = models.ImageField(upload_to='subalbums/',validators=[validate_image_file,validate_file_for_malicious_content])

    class Meta:
      verbose_name = 'Wind Turbine photo'


# 
class depart_documents(models.Model):
    Description	 = models.CharField(max_length=100,validators=[alphanumeric],blank=False,null=True)
    Version = models.DecimalField(max_digits=10, decimal_places=2)
    Download	 = models.FileField(upload_to='departs/',blank=False,validators=[validate_pdf_file,validate_file_for_malicious_content])

    class Meta:
      verbose_name = 'Department document'


# Skill_developements_training
class Skill_developements_training(models.Model):
    title = models.CharField(max_length=255, validators=[alphanumeric],blank=False,null=True) # max_length is required
    description = HTMLField(null=True, blank=True,validators=[validate_forbidden_html_tags])

    class Meta:
      verbose_name = 'Skill developement training'

class Department_Fna_Purchase(models.Model):
    annexure=models.CharField(max_length=200,validators=[alphanumeric],blank=False,null=True)
    docs = models.FileField(upload_to='departs/',blank=False,validators=[validate_pdf_file,validate_file_for_malicious_content])

    class Meta:
      verbose_name = 'Department F&a Purchase'
    
class Department_Fna_Finance(models.Model):
    title = models.CharField(max_length=200,validators=[alphanumeric],blank=False,null=True)
    docs = models.FileField(upload_to='departs/',blank=False,validators=[validate_pdf_file,validate_file_for_malicious_content])

    class Meta:
      verbose_name = 'Department F&a Finance'


class Department_testing_measure(models.Model): 
    title = models.CharField(max_length=100,validators=[alphanumeric],blank=False,null=True)

    class Meta:
      verbose_name = 'Department testing measure'

class Department_testing_measureType(models.Model):
    item = models.ForeignKey(Department_testing_measure, on_delete=models.CASCADE)
    s_no = models.PositiveIntegerField()
    year = models.CharField(max_length=4,validators=[only_numbers])
    project_number = 	 models.CharField(max_length=100,validators=[alphanumeric],blank=False,null=True)
    testing_type_with_company_name = models.CharField(max_length=100,validators=[alphanumeric],blank=False,null=True)
    agreement_signed = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
      verbose_name = 'Department-Testing measureType'
   
    def __str__(self):
        return f"Department-testing  of {self.item.title}"


class SDT_Customize_Training(models.Model):
    serial = models.IntegerField()
    title = models.CharField(validators=[alphanumeric],blank=False,null=True)   

    class Meta:
      verbose_name = 'SDT Customize Training'
    


class SDT_Customize_Training_Sub(models.Model):
    item = models.ForeignKey(SDT_Customize_Training, on_delete=models.CASCADE)
    title = models.CharField(validators=[alphanumeric],blank=False,null=True)
    data = HTMLField(null=True, blank=False,validators=[validate_forbidden_html_tags])

    def __str__(self):
        return f"National-training  of {self.item.title}"
 
    
class SDT_Webinar(models.Model):
    title = models.CharField(max_length=255,validators=[alphanumeric],blank=False,null=True)
    image = models.ImageField(upload_to='images/',blank=False, validators=[validate_image_file])
    docs = models.FileField(upload_to='annual-reports/',blank=False,validators=[validate_pdf_file,validate_file_for_malicious_content])

    class Meta:
      verbose_name = 'SDT Webinar'

    def __str__(self):
        return self.title

    def get_url_url(self):
        return self.docs.url  # Returns the URL of the  uploaded file


class SDT_Short_Term(models.Model):
    title = models.CharField(max_length=255,validators=[alphanumeric])   
    description = HTMLField(null=True, blank=False,validators=[validate_forbidden_html_tags])

    class Meta:
      verbose_name = 'SDT Short Term'

    def __str__(self):
        return self.title

  

class SDT_GlobalWindDay(models.Model):
    serial = models.IntegerField()
    title = models.CharField(max_length=255,validators=[alphanumeric],blank=False,null=True)    
    type = models.CharField(max_length=200, default='url',validators=[alphanumeric],blank=False,null=True, help_text="Enter as docs if PDF is to link, otherwise type url ")
    docs = models.FileField(null=True, blank=True,validators=[validate_pdf_file,validate_file_for_malicious_content])

    class Meta:
      verbose_name = 'SDT Global WindDay'

    def __str__(self):
     return self.title


class SDT_Global_Sub_Wind(models.Model):
    item = models.ForeignKey(SDT_GlobalWindDay, on_delete=models.CASCADE)
    title = models.CharField(max_length=255,validators=[alphanumeric],blank=True,null=True)
    description = HTMLField(null=True, blank=True,validators=[validate_forbidden_html_tags])


class SDT_Iredas_News(models.Model):
    serial = models.IntegerField()
    year = models.IntegerField(unique=True)
    title = models.CharField(max_length=255, validators=[alphanumeric],blank=False,null=True)

    class Meta:
      verbose_name = 'SDT Ireda News'
    
    def __str__(self):
     return self.title


class SDT_Iredas_Sub_News(models.Model):
    item = models.ForeignKey(SDT_Iredas_News, on_delete=models.CASCADE)
    title = models.CharField(max_length=255,validators=[alphanumeric],blank=False,null=True)
    description = HTMLField(null=True, blank=True,validators=[validate_forbidden_html_tags])




class SDT_workshop(models.Model):
    title = models.CharField(max_length=255, validators=[alphanumeric],blank=False,null=True)
    subTitle = models.CharField(max_length=255,validators=[alphanumeric],blank=False,null=True)  # max_length is required

    class Meta:
      verbose_name = 'SDT Workshop'


class SDT_workshop_type(models.Model):
    item = models.ForeignKey(SDT_workshop, on_delete=models.CASCADE)    
    image = models.ImageField(upload_to='images/',validators=[validate_image_file,validate_file_for_malicious_content])

    def __str__(self):
        return f"workshop-testing  of {self.item.title}"
   


class SDT_National(models.Model):
    serial = models.CharField(max_length=7, validators=[alphanumeric], blank=False, null=True)
    title = models.CharField(max_length=200, validators=[alphanumeric], blank=False, null=True)
    slug = models.SlugField(max_length=50,unique=True, blank=False, null=True)
    New_Label = models.BooleanField(default=False,blank=True)

    class Meta:
        verbose_name = 'SDT National'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f" NTC{self.serial}")  # Automatically generate slug from title
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class SDT_National_Page(models.Model):
    item = models.ForeignKey(SDT_National, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,validators=[alphanumeric], blank=False, null=True)
    data = HTMLField(null=True, blank=False,validators=[validate_forbidden_html_tags])

    def __str__(self):
        return f"National-training  of {self.item.title}"


class SDT_Eitc_Trainings(models.Model):
    serial = models.CharField(max_length=100,validators=[alphanumeric], blank=False, null=True)
    project_title = models.CharField(max_length=200,validators=[alphanumeric], blank=False, null=True)
    no_of_country = models.PositiveIntegerField()
    no_of_participants = models.PositiveIntegerField()

    class Meta:
      verbose_name = 'SDT E-ITEC Trainings'

    def __str__(self):
        return self.serial


class SDT_Eitc_Sub_Training(models.Model):
    item = models.ForeignKey(SDT_Eitc_Trainings, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,validators=[alphanumeric], blank=False, null=True)
    data = HTMLField( blank=True,validators=[validate_forbidden_html_tags])

    def __str__(self):
        return f" Training  of {self.item.project_title}"


class SDT_Training_calender(models.Model):
    training_type = models.CharField(max_length=100, default='Default Training Type',validators=[alphanumeric], blank=False, null=True)
    serial = models.IntegerField()
    description = models.CharField(max_length=255,validators=[alphanumeric], blank=False, null=True)
    date_from = models.DateField(auto_now=False, auto_now_add=False)
    date_To = models.DateField(auto_now=False, auto_now_add=False)
    duration = models.CharField(max_length=200,validators=[alphanumeric], blank=False, null=True)

    class Meta:
      verbose_name = 'SDT Training calender'
    

class SDT_Training_Sub_calender(models.Model):
    item = models.ForeignKey(SDT_Training_calender, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, validators=[alphanumeric], blank=False, null=True)
    data = HTMLField( blank=True,validators=[validate_forbidden_html_tags])

    def __str__(self):
        return f"Training-Calender  of {self.item.description}"


class SDT_InternationalTraining(models.Model):
    title = models.CharField(max_length=100, validators=[alphanumeric], blank=False, null=True)
    slug = models.SlugField(unique=True, blank=True)  # Add slug field
    image = models.ImageField(upload_to='annual-reports/', validators=[validate_image_file,validate_file_for_malicious_content])

    class Meta:
      verbose_name = 'SDT International Training'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class SDT_InternationalTraining_eitec(models.Model):
    item = models.ForeignKey(SDT_InternationalTraining, on_delete=models.CASCADE)
    serial = models.IntegerField()
    title = models.CharField(max_length=200, validators=[alphanumeric], blank=False, null=True)
    slug = models.SlugField(unique=True, blank=True)  # Add slug field
  
    def __str__(self):
        return f"{self.serial}. {self.title} ({self.item.title})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class SDT_InternationalTraining_sub_eitec(models.Model):
    eitec = models.ForeignKey(SDT_InternationalTraining_eitec, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,validators=[alphanumeric], blank=False, null=True)
    slug = models.SlugField(unique=True, blank=True)  # Add slug field
    data = HTMLField(null=True, blank=True, validators=[validate_forbidden_html_tags])

    def __str__(self):
        return f"International Sub EITEC training of {self.eitec.item.title} - {self.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    
class SDT_vayumitra(models.Model):
    serial = models.IntegerField()
    title = models.CharField(max_length=255,validators=[alphanumeric], blank=False, null=True)
    type= models.CharField(max_length=10, validators=[alphanumeric], blank=False, null=True)    
    urls = models.URLField(max_length=200, blank=True, null=True,)
    docs = models.FileField(upload_to='annual-reports/', null=True, blank=True,validators=[validate_pdf_file,validate_file_for_malicious_content])

    class Meta:
      verbose_name = 'SDT vayumitra'

    def __str__(self):
        return self.title

class SDT_Library(models.Model):
    title_type = models.CharField(max_length=50, default='Library Type',validators=[alphanumeric], blank=False, null=True)
    serial = models.IntegerField()
    title_of_magzines = models.CharField(max_length=200,validators=[alphanumeric], blank=False, null=True)
    subcription_status = models.CharField(max_length=50, blank=True, validators=[alphanumeric],  null=True)

    class Meta:
      verbose_name = 'SDT Library'
    

# 
#  Wind_Resources_Assessment
class Wind_Resources_Assessment(models.Model):
    title = models.CharField(max_length=255,validators=[alphanumeric], blank=False, null=True)
    description = HTMLField( blank=False,validators=[validate_forbidden_html_tags])

    class Meta:
      verbose_name = 'Wind Resources Assessment'


class WRA_Sale_publication(models.Model):
    serial = models.IntegerField()
    product = models.CharField(max_length=250,validators=[alphanumeric], blank=False, null=True)
    price = models.CharField(max_length=250,validators=[alphanumeric], blank=False, null=True)
    total_amount1 = models.CharField(max_length=250,validators=[alphanumeric], blank=False, null=True)
    total_amount2 = models.CharField( blank=True,default=" ",validators=[alphanumeric],  null=True)   
    charge = models.CharField(max_length=50,validators=[alphanumeric], blank=True, null=True)
    remarks = HTMLField(blank=False,null=True,validators=[validate_forbidden_html_tags])
    class Meta:
      verbose_name = 'WRA Sale publication'


class WRA_srra_stations(models.Model):
    serial = models.IntegerField()
    state_ut = models.CharField(max_length=250,validators=[alphanumeric], blank=True, null=True)
    phase1 = models.CharField(max_length=250,validators=[alphanumeric], blank=True, null=True)
    phase2 = models.CharField(max_length=250,validators=[alphanumeric], blank=True, null=True)
    ams = models.CharField(max_length=250,validators=[alphanumeric], blank=True, null=True)
    meda = models.CharField(max_length=250,validators=[alphanumeric], blank=True, null=True)
    anert = models.CharField(max_length=250,validators=[alphanumeric], blank=True, null=True)
    total = models.CharField(max_length=250,validators=[alphanumeric], blank=True, null=True)

    class Meta:
      verbose_name = 'WRA srra stations'


class WRA_Numeric_Wind(models.Model):
    serial = models.IntegerField()
    domain = models.CharField(max_length=250,validators=[alphanumeric], blank=False, null=True)
    number_station = models.IntegerField()
    error_of_wind_speed = models.DecimalField(max_digits=10, decimal_places=2,blank=False, null=True)

    class Meta:
      verbose_name = 'WRA Numeric Wind'


class WRA_Micro_Servey(models.Model):
    serial = models.IntegerField()
    state = models.CharField(max_length=250,validators=[alphanumeric],blank=False, null=True)
    stations = models.IntegerField()

    class Meta:
      verbose_name = 'WRA Micro Survey'


class WRA_Estimated_Potential(models.Model):
    serial = models.IntegerField(blank=False, null=False)
    state_ut = models.CharField(max_length=250,validators=[alphanumeric],blank=False, null=True)
    potential_50m = models.IntegerField(blank=True, null=True)
    potential_80m = models.IntegerField(blank=True, null=True)
  

    class Meta:
      verbose_name = 'WRA Estimated Potential'


class WRA_Srra_Station_phases(models.Model):
    
    station_id = models.IntegerField(blank=False)
    station_name = models.CharField(max_length=250,validators=[alphanumeric],blank=False, null=True)
    location = models.CharField(max_length=250,validators=[alphanumeric],blank=False, null=True)
    district = models.CharField(max_length=250,validators=[alphanumeric],blank=False, null=True)
    state = models.CharField(max_length=250,validators=[alphanumeric],blank=False, null=True)
    comission_date = models.DateField(auto_now=False, auto_now_add=False)
    latitude = models.DecimalField(max_digits=10, decimal_places=3)
    longitude = models.DecimalField(max_digits=10, decimal_places=3)
    elavation = models.IntegerField()  

    class Meta:
      verbose_name = 'WRA Srra Station phases'


class WRA_Srra_Station_phaseII(models.Model):
    
    station_id = models.IntegerField(blank=False)
    station_name = models.CharField(max_length=250,validators=[alphanumeric],blank=False, null=True)
    location = models.CharField(max_length=250,validators=[alphanumeric],blank=False, null=True)
    district = models.CharField(max_length=250,validators=[alphanumeric],blank=False, null=True)
    state = models.CharField(max_length=250,validators=[alphanumeric],blank=False, null=True)
    comission_date = models.DateField(auto_now=False, auto_now_add=False)
    latitude = models.DecimalField(max_digits=10, decimal_places=3)
    longitude = models.DecimalField(max_digits=10, decimal_places=3)
    elavation = models.IntegerField(blank=False)  

    class Meta:
      verbose_name = 'WRA Srra Station phaseII'

    
class WRA_Srra_Station_meda(models.Model):
    
    station_id = models.IntegerField(blank=False)
    station_name = models.CharField(max_length=250,validators=[alphanumeric],blank=False, null=True)
    location = models.CharField(max_length=250,validators=[alphanumeric],blank=False, null=True)
    district = models.CharField(max_length=250,validators=[alphanumeric],blank=False, null=True)
    state = models.CharField(max_length=250,validators=[alphanumeric],blank=False, null=True)
    comission_date = models.DateField(auto_now=False, auto_now_add=False)
    latitude = models.DecimalField(max_digits=10, decimal_places=3)
    longitude = models.DecimalField(max_digits=10, decimal_places=3)
    elavation = models.IntegerField(blank=False)  

    class Meta:
      verbose_name = 'WRA Srra Station meda'


class WRA_Srra_Station_anert(models.Model):
    
    station_id = models.IntegerField(blank=False)
    station_name = models.CharField(max_length=250,validators=[alphanumeric],blank=False, null=True)
    location = models.CharField(max_length=250,validators=[alphanumeric],blank=False, null=True)
    district = models.CharField(max_length=250,validators=[alphanumeric],blank=False, null=True)
    state = models.CharField(max_length=250,validators=[alphanumeric],blank=False, null=True)
    comission_date = models.DateField(auto_now=False, auto_now_add=False)
    latitude = models.DecimalField(max_digits=10, decimal_places=3)
    longitude = models.DecimalField(max_digits=10, decimal_places=3)
    elavation = models.IntegerField(blank=False)  

    class Meta:
      verbose_name = 'WRA Srra Station ANERT'

    
class WRA_Srra_Station_ams(models.Model):
    
    station_id = models.IntegerField(blank=False)
    station_name = models.CharField(max_length=250,validators=[alphanumeric],blank=False, null=True)
    location = models.CharField(max_length=250,validators=[alphanumeric],blank=False, null=True)
    district = models.CharField(max_length=250,validators=[alphanumeric],blank=False, null=True)
    state = models.CharField(max_length=250,validators=[alphanumeric],blank=False, null=True)
    comission_date = models.DateField(auto_now=False, auto_now_add=False)
    latitude = models.DecimalField(max_digits=10, decimal_places=3)
    longitude = models.DecimalField(max_digits=10, decimal_places=3)
    elavation = models.IntegerField(blank=False)  

    class Meta:
      verbose_name = 'WRA Srra Station AMS'


# owd
class Offshore_Wind_Development(models.Model):
    title = models.CharField(max_length=250,validators=[alphanumeric],blank=False, null=True)
    description = HTMLField(blank=False,validators=[validate_forbidden_html_tags])

    class Meta:
      verbose_name = 'Offshore Wind Development'



#  finance
class Finance_and_Administration(models.Model):

    description = HTMLField( blank=True,validators=[validate_forbidden_html_tags])
    NIWE_Pan_ARN_GST_Details = HTMLField( blank=True,validators=[validate_forbidden_html_tags])

    class Meta:
      verbose_name = 'Finance and Administration'
    
class WindPotentialSite(models.Model):
    state_name = models.CharField(max_length=255, unique=True, validators=[alphanumeric],blank=False, null=False)  # User can enter any state name
    jpg_map = models.ImageField(upload_to='maps/jpg/', blank=True, null=True,validators=[validate_image_file])
    kml_file = models.FileField(upload_to='maps/kml/', blank=True, null=True, validators=(FileExtensionValidator(['kml','kmz']), validate_filename ))


    def __str__(self):
        return self.state_name
    
    class Meta:
      verbose_name = 'Wind Potential Site'
   

   