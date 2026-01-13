# views.py
from django.shortcuts import render
from about_section.models import AboutUs, DirectorGeneralMessage, Background, charter, OrganizationalChart, QualityPolicy
from certification_services.models import Certification_Procedure
from Media_Section.models import Award, Citizen_Charter, Events, Gallery, Think_Tank
from Depart_Section.models import Departments, Reserach_n_Development, Finance_and_Administration, Department_Fna_Finance, Offshore_Wind_Development,  Department_testing_measure,  Department_Fna_Purchase, Testing_and_Standards_Regulation,Wind_Resources_Assessment, Skill_developements_training, Wind_Terbine_photo, depart_documents
from Document_Section.models import * 
from .forms import SearchForm

def search(request):
    form = SearchForm()
    # for about_section
    aboutUs = []
    background = []
    DGMessage= []
    charters= []
    OrgChart = []
    qualityPolicy=[]
    
    #  for media section
    award = []
    citizen_charter= []
    events= []
    gallery= []
    thin_tank= []
    
    # for department_sections
    departments = [] 
    certification_procedure = []
    research_development = []
    finance_development= []
    finance_administration= [] 
    finance_purchase = []
    department_Testing= []
    depart_document=[]
    depart_skill_development= []
    
    depart_owd= []
    depart_wind_resource =[]
    
# for Document_section

    genral_info= []
    annual_report=[]
    newsletters= []
    related_links= []
    record_retention=[]    
    weg_Install_world=[]
    revised_guidelines = []
    weg_Install_India = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            # Search in About_section models
            aboutUs = AboutUs.objects.filter(title__icontains=query) | AboutUs.objects.filter(description__icontains=query)
            background = Background.objects.filter(description__icontains=query)
            DGMessage =DirectorGeneralMessage.objects.filter(title__icontains=query) | DirectorGeneralMessage.objects.filter(description__icontains=query) | DirectorGeneralMessage.objects.filter(Dirs_image__icontains=query)  
            charters  = charter.objects.filter(preamble__icontains=query) | charter.objects.filter(mission__icontains=query) | charter.objects.filter(objectives__icontains=query)
            OrgChart = OrganizationalChart.objects.filter(description__icontains=query) | OrganizationalChart.objects.filter(image__icontains=query)
            qualityPolicy =   QualityPolicy.objects.filter(policyImage__icontains=query)


            # Search in media_section models
            award=   Award.objects.filter(title__icontains=query)  | Award.objects.filter(description__icontains=query) | Award.objects.filter(image_1__icontains=query) | Award.objects.filter(image_2__icontains=query)
            citizen_charter=   Citizen_Charter.objects.filter(title__icontains=query) | Citizen_Charter.objects.filter(document_File__icontains=query)  
            events=   Events.objects.filter(title__icontains=query) | Events.objects.filter(document_File__icontains=query) | Events.objects.filter(url__icontains=query)
            gallery=   Gallery.objects.filter(title__icontains=query) | Gallery.objects.filter(cover_image__icontains=query)
            thin_tank=   Think_Tank.objects.filter(title__icontains=query)
            
            # Search in Department model
            departments = Departments.objects.filter(title__icontains=query) | Departments.objects.filter(description__icontains=query)
            research_development  = Reserach_n_Development.objects.filter(title__icontains=query) | Reserach_n_Development.objects.filter(description__icontains=query)
            finance_development  = Department_Fna_Finance.objects.filter(title__icontains=query) | Department_Fna_Finance.objects.filter(docs__icontains=query)
            finance_administration  = Finance_and_Administration.objects.filter(description__icontains=query) | Finance_and_Administration.objects.filter(NIWE_Pan_ARN_GST_Details__icontains=query)
            depart_document  = depart_documents.objects.filter(Description__icontains=query)
            depart_skill_development  = Skill_developements_training.objects.filter(title__contains=query)
            depart_owd  = Offshore_Wind_Development.objects.filter(title__icontains=query) | Offshore_Wind_Development.objects.filter(description__icontains=query)
            # depart_wind_resource  = Wind_Resources_Assessment.objects.filter(title_icontains=query) | Wind_Resources_Assessment.objects.filter(description__icontains=query)

            finance_purchase = Department_Fna_Purchase.objects.filter(annexure__icontains=query)
            department_Testing=Testing_and_Standards_Regulation.objects.filter(title__icontains=query) | Testing_and_Standards_Regulation.objects.filter(description__icontains=query)

            # Search in Department model
            certification_procedure = Certification_Procedure.objects.filter(title__icontains=query) | Certification_Procedure.objects.filter(description__icontains=query)

            # for Document_section
            genral_info=  GeneralInformation.objects.filter(title__icontains=query) | GeneralInformation.objects.filter(description__icontains=query)
            # annual_report=  AnnualReport.objetcs.filter(year__icontains=query)
            newsletters=  Newsletters.objects.filter(issue__icontains=query) | Newsletters.objects.filter(year__icontains=query)
            weg_Install_world = weg_install_world_wise.objects.filter(position__icontains=query) | weg_install_world_wise.objects.filter(country__icontains=query) | weg_install_world_wise.objects.filter(capacity__icontains=query)
            weg_Install_India= WEG_Installation_Details_India.objects.filter(sr_no__icontains=query) | WEG_Installation_Details_India.objects.filter(state__icontains=query) | WEG_Installation_Details_India.objects.filter(upto_31_03_2002__icontains=query) | WEG_Installation_Details_India.objects.filter(year_2002_03__icontains=query) | WEG_Installation_Details_India.objects.filter(year_2003_04__icontains=query) | WEG_Installation_Details_India.objects.filter(year_2004_05__icontains=query) | WEG_Installation_Details_India.objects.filter(year_2005_06__icontains=query)
            revised_guidelines = RevisedGuidelineForProject.objects.filter(sr_No__icontains=query) | RevisedGuidelineForProject.objects.filter(description__icontains=query) | RevisedGuidelineForProject.objects.filter(date__icontains=query)
            related_links=  RelatedLinks.objects.filter(title__icontains=query) | RelatedLinks.objects.filter(linkTitle__icontains=query) 
            record_retention=  RecordsRetentionSchedule.objects.filter(ministry_Approval__icontains=query)
                    
    return render(request, 'search_results.html', {
        'form': form,
        # for about 
        'aboutUs': aboutUs,
        'background': background,
        'DGMessage' : DGMessage,
        'charters': charters,
        'OrgChart' : OrgChart, 
        'qualityPolicy' : qualityPolicy,
        
        # for media_section
        
        'award' : award,
        'citizen_charter': citizen_charter,
        'events' : events,
        'gallery': gallery,
        'thin_tank': thin_tank,
        
        # for department_section
        
        'departments': departments,
        'research_development' : research_development,
        'finance_development':finance_development,
        'finance_administration': finance_administration,
        'finance_purchase': finance_purchase,

        'depart_document': depart_document, 
        'depart_skill_development': depart_skill_development,
        'depart_owd': depart_owd,
        'depart_wind_resource' :depart_wind_resource,
        'department_Testing': department_Testing,
        
        'certification_procedure': certification_procedure,
        
        # for Document_section
        'genral_info' :genral_info,
        'annual_report' : annual_report,
        'newsletters' : newsletters,
        'weg_Install_world' : weg_Install_world,
        'revised_guidelines' : revised_guidelines,
        'related_links' : related_links,
        'record_retention' : record_retention,
        'weg_Install_India': weg_Install_India,

    })
