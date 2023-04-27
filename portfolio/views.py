from django.shortcuts import render
from .models import User, Projects, Skills, SocialMediaAccount, Resume, Certificate, Gallary

# Create your views here.
def index(request):
    context = {
        'user': User.objects.first(),
        'projects': Projects.objects.all(),
        'skills': Skills.objects.all(),
        'social_media_accounts': SocialMediaAccount.objects.all(),
        'resume': Resume.objects.first(),
        'certificates': Certificate.objects.all(),
        'gallary': Gallary.objects.all(),
    }
    return render(request,'index.html',context)

def contact(request):
    return render(request,'contact.html',{})