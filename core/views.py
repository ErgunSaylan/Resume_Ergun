from django.shortcuts import render, redirect, get_object_or_404

from core.admin import SocialMediaAdmin
from core.models import GeneralSetting, ImageSetting, Skill, Resume, Sumary, Project, Certificate, SocialMedia, Document


# Create your views here.

def index(request):
    site_title = GeneralSetting.objects.get(name='site_title').parameter
    site_keywords = GeneralSetting.objects.get(name='site_keywords').parameter
    site_description = GeneralSetting.objects.get(name='site_description').parameter
    about_description = GeneralSetting.objects.get(name='about_description').parameter
    home_banner_name = GeneralSetting.objects.get(name='home_banner_name').parameter
    job_description = GeneralSetting.objects.get(name='job_description').parameter
    about_me = GeneralSetting.objects.get(name='about_me').parameter
    about_education = GeneralSetting.objects.get(name='about_education').parameter
    resume_description = GeneralSetting.objects.get(name='resume_description').parameter

    #images
    home_banner_image = ImageSetting.objects.get(name='home_banner_image').file
    site_favicon = ImageSetting.objects.get(name='site_favicon').file

    #Skills
    skills = Skill.objects.all().order_by('order')

    #Sumary
    Sumaries = Sumary.objects.all()
    #Education
    Resumes = Resume.objects.all()

    #Projects
    Projects = Project.objects.all()
    #Certificates
    Certificates = Certificate.objects.all()
    #SocialMedias
    SocialMedias = SocialMedia.objects.all()

    #Document
    Documents = Document.objects.all()
    context= {
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'about_description': about_description,
        'home_banner_name': home_banner_name,
        'job_description': job_description,
        'about_me': about_me,
        'about_education': about_education,
        'home_banner_image': home_banner_image,
        'site_favicon': site_favicon,
        'skills': skills,
        'Resumes': Resumes,
        'resume_description': resume_description,
        'Sumaries': Sumaries,
        'Projects': Projects,
        'Certificates': Certificates,
        'SocialMedias': SocialMedias,
        'Documents': Documents,

    }
    return render(request, 'index.html', context=context)


def redirect_urls(request, slug):
    doc = get_object_or_404(Document, slug=slug)
    return redirect(doc.file.url)