from django.contrib import admin

from models import CommissionedProject, PersonalProject, Employer, Client

admin.site.register(Client)
admin.site.register(Employer)
admin.site.register(CommissionedProject)
admin.site.register(PersonalProject)