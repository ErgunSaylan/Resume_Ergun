from django.shortcuts import render
from core.models import GeneralSetting
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
    context= {
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'about_description': about_description,
        'home_banner_name': home_banner_name,
        'job_description': job_description,
        'about_me': about_me,
        'about_education': about_education,
    }
    return render(request, 'index.html', context=context)

