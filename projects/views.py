from django.template import RequestContext
from django.shortcuts import render_to_response

from mini_cms.models import Taxonomy
from models import PersonalProject, CommissionedProject


def index(request):
    personal_projects = PersonalProject.objects.all()
    paid_projects = CommissionedProject.objects.all()

    # just going to go ahead and require these
    whoami = Taxonomy.objects.get(key='whoami').get_val()
    projects_blurb = Taxonomy.objects.get(key='projects_blurb').get_val()

    data = {
        'personal_projects': personal_projects,
        'paid_projects': paid_projects,
        'whoami': whoami,
        'projects_blurb': projects_blurb
    }
    return render_to_response('index.html', data, RequestContext(request))