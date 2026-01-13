from django.db import models
from NiwaProject.settings import alphanumeric
from NiwaProject.validation_file import validate_image_file,validate_file_for_malicious_content,validate_pdf_for_malicious_content,validate_image_metadata_for_malicious_content,validate_image_for_steganography


class CertificationAndInformationTechnologyStaff(models.Model):
    name = models.CharField(max_length=100, blank=False,null=True,validators=[alphanumeric])
    position = models.CharField(max_length=100,blank=False,null=True,validators=[alphanumeric])
    email = models.CharField(max_length=254, blank=False,null=True,validators=[alphanumeric])
    phone_number = models.CharField(max_length=50, blank=False,null=True,validators=[alphanumeric])
    department = models.CharField(max_length=100, blank=True,null=True,validators=[alphanumeric])
    
    def __str__(self): 
        return self.name

    
class CertificationStaffPhoto(models.Model):
    staff = models.ForeignKey(CertificationAndInformationTechnologyStaff, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='subalbums/', validators=[validate_image_file,validate_file_for_malicious_content])   
    Designation = models.CharField(max_length=100, null=True, blank=True, validators=[alphanumeric])
    Qualification = models.CharField(max_length=100, null=True, blank=True,validators=[alphanumeric])
    Specialization = models.CharField(max_length=254, default="", blank=True,validators=[alphanumeric])
    Areas_Of_Interest = models.CharField(max_length=254, default="", blank=True,validators=[alphanumeric])
    Year_of_Joining = models.CharField(max_length=100, null=True, blank=True,validators=[alphanumeric])
    contact = models.CharField(max_length=100, null=True, blank=True,validators=[alphanumeric])
    email = models.CharField(max_length=254, null=True, blank=True, validators=[alphanumeric])

    def __str__(self):
        return f"CertificationStaff-Photo of {self.staff.name}"


# 
class DirectorGeneralOfficeStaff(models.Model):
    name = models.CharField(max_length=100,blank=False,null=True,validators=[alphanumeric])
    position = models.CharField(max_length=100,blank=False,null=True,validators=[alphanumeric])
    email = models.CharField(max_length=254, blank=False,null=True,validators=[alphanumeric])
    phone_number = models.CharField(max_length=50, blank=False,null=True,validators=[alphanumeric])
    department = models.CharField(max_length=100, blank=True,null=True,validators=[alphanumeric])

    def __str__(self): 
        return self.name


# 
class StaffPhoto(models.Model):
    staff = models.ForeignKey(DirectorGeneralOfficeStaff, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='subalbums/',validators=[validate_image_file,validate_file_for_malicious_content])
        
    Designation = models.CharField(max_length=100, null=True, blank=True,validators=[alphanumeric])
    Qualification = models.CharField(max_length=100, null=True, blank=True,validators=[alphanumeric])
    Specialization = models.CharField(max_length=100, default="", blank=True,validators=[alphanumeric])
    Areas_Of_Interest = models.CharField(max_length=255, default="", blank=True,validators=[alphanumeric])
    Year_of_Joining = models.CharField(max_length=100, null=True, blank=True,validators=[alphanumeric])
    contact = models.CharField(max_length=100, null=True, blank=True,validators=[alphanumeric])
    email = models.CharField(max_length=254,  null=True, blank=True,validators=[alphanumeric])

    def __str__(self):
        return f"Staff-Photo of {self.staff.name}"


    # 
class OffshoreWindDevelopStaff(models.Model):
    name = models.CharField(max_length=100,blank=False,null=True,validators=[alphanumeric])
    position = models.CharField(max_length=100,blank=False,null=True,validators=[alphanumeric])
    email = models.CharField(max_length=254, blank=False,null=True,validators=[alphanumeric])
    phone_number = models.CharField(max_length=50, blank=True,null=True,validators=[alphanumeric])

    def __str__(self): 
        return self.name


class OwdStaffPhoto(models.Model):
    staff = models.ForeignKey(OffshoreWindDevelopStaff, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='subalbums/',validators=[validate_image_file,validate_file_for_malicious_content])
    # 
    Designation = models.CharField(max_length=100, null=True, blank=True,validators=[alphanumeric])
    Qualification = models.CharField(max_length=100, null=True, blank=True,validators=[alphanumeric])
    Specialization = models.CharField(max_length=100, default="", blank=True,validators=[alphanumeric])
    Areas_Of_Interest = models.CharField(max_length=255, default="", blank=True,validators=[alphanumeric])
    Year_of_Joining = models.CharField(max_length=100, null=True, blank=True,validators=[alphanumeric])
    contact = models.CharField(max_length=100, null=True, blank=True,validators=[alphanumeric])
    email = models.CharField(max_length=254, null=True, blank=True,validators=[alphanumeric])
    def __str__(self):
        return f"OwdStaff-Photo of {self.staff.name}"
        

class TestingStandardsAndRegulationStaff(models.Model):
    name = models.CharField(max_length=100,blank=False,null=True,validators=[alphanumeric])
    position = models.CharField(max_length=100,blank=False,null=True,validators=[alphanumeric])
    email = models.CharField(max_length=254,  blank=False,null=True,validators=[alphanumeric])
    phone_number = models.CharField(max_length=50, blank=False,null=True,validators=[alphanumeric])
    department = models.CharField(max_length=100, null=True, blank=True,validators=[alphanumeric])

class TestingStaffPhoto(models.Model):
    staff = models.ForeignKey(TestingStandardsAndRegulationStaff, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='subalbums/',validators=[validate_image_file,validate_file_for_malicious_content])
    Designation = models.CharField(max_length=100, null=True, blank=True,validators=[alphanumeric])
    Qualification = models.CharField(max_length=255,null=True, blank=True,validators=[alphanumeric])
    Specialization = models.CharField( default="", blank=True,validators=[alphanumeric])
    Areas_Of_Interest = models.CharField( default="", blank=True,validators=[alphanumeric])
    Year_of_Joining = models.CharField(max_length=100, null=True, blank=True,validators=[alphanumeric])
    contact = models.CharField(max_length=100, null=True, blank=True,validators=[alphanumeric])
    email = models.CharField(max_length=254, null=True, blank=True,validators=[alphanumeric])
    def __str__(self):
        return f"TestingStaff-Photo of {self.staff.name}"

# 
class ResearchAndDevelopmentStaff(models.Model):
    name = models.CharField(max_length=100,blank=False,null=True,validators=[alphanumeric])
    position = models.CharField(max_length=100,blank=False,null=True,validators=[alphanumeric])
    email = models.CharField(max_length=254, blank=False,null=True,validators=[alphanumeric])
    phone_number = models.CharField(max_length=50, blank=True, validators=[alphanumeric])
    
   
class ResearchStaffPhoto(models.Model):
    staff = models.ForeignKey(ResearchAndDevelopmentStaff, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='subalbums/',validators=[validate_image_file,validate_file_for_malicious_content])   
    Designation = models.CharField(max_length=100, null=True, blank=True, validators=[alphanumeric])
    Qualification = models.CharField(max_length=100, null=True, blank=True, validators=[alphanumeric])
    Specialization = models.CharField(max_length=100, default="", blank=True, validators=[alphanumeric])
    Areas_Of_Interest = models.CharField(max_length=255, default="", blank=True, validators=[alphanumeric])
    Year_of_Joining = models.CharField(max_length=100, null=True, blank=True, validators=[alphanumeric])
    contact = models.CharField(max_length=100, null=True, blank=True, validators=[alphanumeric])
    email = models.CharField(max_length=254, null=True, blank=True, validators=[alphanumeric])

    def __str__(self):
        return f"ResearchStaff-Photo of {self.staff.name}"


class WindResourceAssessmentStaff(models.Model):
    name = models.CharField(max_length=100,blank=False,null=True,validators=[alphanumeric])
    position = models.CharField(max_length=100,blank=False,null=True,validators=[alphanumeric])
    email = models.CharField(max_length=254, blank=False,null=True,validators=[alphanumeric])
    phone_number = models.CharField(max_length=50, blank=False,null=True,validators=[alphanumeric])


class WRAStaffPhoto(models.Model):
    staff = models.ForeignKey(WindResourceAssessmentStaff, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='subalbums/',validators=[validate_image_file,validate_file_for_malicious_content]) 
    Designation = models.CharField(max_length=100, null=True, blank=True,validators=[alphanumeric])
    Qualification = models.CharField(max_length=100, null=True, blank=True,validators=[alphanumeric])
    Specialization = models.CharField(max_length=100, default="", blank=True,validators=[alphanumeric])
    Areas_Of_Interest = models.CharField(max_length=255, default="", blank=True,validators=[alphanumeric])
    Year_of_Joining = models.CharField(max_length=100, null=True, blank=True,validators=[alphanumeric])
    contact = models.CharField(max_length=100, null=True, blank=True,validators=[alphanumeric])
    email = models.CharField(max_length=254, unique=True, null=True, blank=True,validators=[alphanumeric])

    def __str__(self):
        return f"WRAStaff-Photo of {self.staff.name}"
# 
class SkillDevelopmentAndTrainingStaff(models.Model):
    name = models.CharField(max_length=100,blank=False,null=True,validators=[alphanumeric])
    position = models.CharField(max_length=100,blank=False,null=True,validators=[alphanumeric])
    email = models.CharField(max_length=254, blank=False,null=True,validators=[alphanumeric])
    phone_number = models.CharField(max_length=50,blank=False,null=True,validators=[alphanumeric])

class SDTStaffPhoto(models.Model):
    staff = models.ForeignKey(SkillDevelopmentAndTrainingStaff, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='subalbums/',validators=[validate_image_file,validate_file_for_malicious_content])
    Designation = models.CharField(max_length=100, null=True, blank=True,validators=[alphanumeric])
    Qualification = models.CharField(max_length=100, null=True, blank=True,validators=[alphanumeric])
    Specialization = models.CharField(max_length=100, default="", blank=True,validators=[alphanumeric])
    Areas_Of_Interest = models.CharField(max_length=255, default="", blank=True,validators=[alphanumeric])
    Year_of_Joining = models.CharField(max_length=100, null=True, blank=True,validators=[alphanumeric])
    contact = models.CharField(max_length=100, null=True, blank=True,validators=[alphanumeric])
    email = models.CharField(max_length=254, unique=True, null=True, blank=True,validators=[alphanumeric])

    def __str__(self):
        return f"SDTStaff-Photo of {self.staff.name}"

# 
class FinanceAndAdministrationStaff(models.Model):
    name = models.CharField(max_length=100,blank=False,null=True,validators=[alphanumeric])
    position = models.CharField(max_length=100,blank=False,null=True,validators=[alphanumeric])
    email = models.CharField(max_length=254, unique=True, blank=False,null=True,validators=[alphanumeric])
    phone_number = models.CharField(max_length=50, blank=False,null=True,validators=[alphanumeric])
    department = models.CharField(max_length=100, null=True, blank=True,validators=[alphanumeric])

class FinanceStaffPhoto(models.Model):
    staff = models.ForeignKey(FinanceAndAdministrationStaff, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='subalbums/',validators=[validate_image_file,validate_file_for_malicious_content])
  
    Designation = models.CharField(max_length=100, null=True, blank=True,validators=[alphanumeric])
    Qualification = models.CharField(max_length=100, null=True, blank=True,validators=[alphanumeric])
    Specialization = models.CharField(max_length=100, default="", blank=True,validators=[alphanumeric])
    Areas_Of_Interest = models.CharField(max_length=255, default="", blank=True,validators=[alphanumeric])
    Year_of_Joining = models.CharField(max_length=100, null=True, blank=True,validators=[alphanumeric])
    contact = models.CharField(max_length=100, null=True, blank=True,validators=[alphanumeric])
    email = models.CharField(max_length=254, unique=True, null=True, blank=True,validators=[alphanumeric])

    def __str__(self):
        return f"FinanceStaff-Photo of {self.staff.name}"
    
class TestingStaff(models.Model):
    name = models.CharField(max_length=100,blank=False,null=True,validators=[alphanumeric])
    position = models.CharField(max_length=100,blank=False,null=True,validators=[alphanumeric])
    email = models.CharField(max_length=254, blank=False,null=True,validators=[alphanumeric])
    phone_number = models.CharField(max_length=50, blank=False,null=True,validators=[alphanumeric])


class TestingDepartStaffPhoto(models.Model):
    staff = models.ForeignKey(TestingStaff, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='subalbums/',validators=[validate_image_file,validate_file_for_malicious_content]) 
    Designation = models.CharField(max_length=100, null=True, blank=True,validators=[alphanumeric])
    Qualification = models.CharField(max_length=255, null=True, blank=True,validators=[alphanumeric])
    Specialization = models.CharField(max_length=100, default="", blank=True,validators=[alphanumeric])
    Areas_Of_Interest = models.CharField(max_length=255, default="", blank=True,validators=[alphanumeric])
    Year_of_Joining = models.CharField(max_length=100, null=True, blank=True,validators=[alphanumeric])
    contact = models.CharField(max_length=100, null=True, blank=True,validators=[alphanumeric])
    email = models.CharField(max_length=254, unique=True, null=True, blank=True,validators=[alphanumeric])

    def __str__(self):
        return f"TestingStaff-Photo of {self.staff.name}"