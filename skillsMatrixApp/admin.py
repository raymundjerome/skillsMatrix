from django.contrib import admin
from .models import employee, skills, organization, skillsMatrix

admin.site.register(employee)
admin.site.register(skills)
admin.site.register(organization)
admin.site.register(skillsMatrix)