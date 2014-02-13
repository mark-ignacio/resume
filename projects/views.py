from django.template import RequestContext
from django.shortcuts import render_to_response

from mini_cms.models import Taxonomy
from models import PersonalProject, CommissionedProject, Employer


def index(request):
    personal_projects = PersonalProject.objects.all()
    paid_projects = CommissionedProject.objects.select_related('employer').all()
    employers = Employer.objects.filter(commissionedproject__in=paid_projects).distinct()

    # just going to go ahead and require these
    whoami = Taxonomy.objects.get(key='whoami').get_val()
    projects_blurb = Taxonomy.objects.get(key='projects_blurb').get_val()

    data = {
        'personal_projects': personal_projects,
        'paid_projects': paid_projects,
        'employers': employers,
        'whoami': whoami,
        'projects_blurb': projects_blurb
    }
    return render_to_response('index.html', data, RequestContext(request))