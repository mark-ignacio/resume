from django.template import RequestContext
from django.shortcuts import render_to_response

from models import PersonalProject, CommissionedProject, Employer


def index(request):
    personal_projects = PersonalProject.objects.all()
    paid_projects = CommissionedProject.objects.select_related('employer').all()
    employers = Employer.objects.filter(commissionedproject__in=paid_projects).distinct()

    data = {
        'personal_projects': personal_projects,
        'paid_projects': paid_projects,
        'employers': employers,
    }
    return render_to_response('index.html', data, RequestContext(request))