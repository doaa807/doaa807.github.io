from django.contrib import admin
from .models import User, Projects, Skills, SocialMediaAccount, Resume, Certificate, Gallary
# Register your models here.

admin.site.register(User)
admin.site.register(Projects)
admin.site.register(Skills)
admin.site.register(SocialMediaAccount)
admin.site.register(Resume)
admin.site.register(Certificate)
admin.site.register(Gallary)
