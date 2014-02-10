from django.template import RequestContext
from models import PersonalProject, CommissionedProject
from django.shortcuts import render_to_response


def index(request):
    personal_projects = PersonalProject.objects.all()
    paid_projects = CommissionedProject.objects.all()

    data = {
        'personal_projects': personal_projects,
        'paid_projects': paid_projects
    }
    return render_to_response('index.html', data, RequestContext(request))