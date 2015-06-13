from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

from django.http import HttpResponse
# from django.template import RequestContext, loader

from .models import Incident
from .models import DirectImpact
from .models import IndirectImpact
from .models import Impact
from .models import IncidentChange
from .models import Means
from .models import SeverityOfImpact
from .models import Source
from .models import Victim
from .models import VictimSector

def index(request):
    latest_incident_list = Incident.objects.all()
    # output = ', '.join([p.Title for p in latest_incident_list])
    # return HttpResponse(output)
    # template = loader.get_template('CPSIDapp/index.html')
    context = {'latest_incident_list': latest_incident_list}
    # return HttpResponse(template.render(context))
    return render(request, 'CPSIDapp/index.html', context)

def incidentDetail(request, id):
    # return HttpResponse("You're looking at incident number %s." % id)
    tempid = id
    current_incident = Incident.objects.filter(id=tempid)
    current_indirectImpact = IndirectImpact.objects.filter(IncidentID_id=tempid)
    current_directImpact = DirectImpact.objects.filter(IncidentID_id=tempid)
    current_impact = Impact.objects.filter(IncidentID_id=tempid)
    current_incidentChange = IncidentChange.objects.filter(IncidentID_id=tempid)
    current_means = Means.objects.filter(IncidentID_id=tempid)
    current_severityOfImpact = SeverityOfImpact.objects.filter(IncidentID_id=tempid)
    current_source = Source.objects.filter(IncidentID_id=tempid)
    current_victim = Victim.objects.filter(IncidentID_id=tempid)
    current_victimSector = VictimSector.objects.filter(IncidentID_id=tempid)
    context = {'current_incident': current_incident, 
    'current_indirectImpact': current_indirectImpact, 
    'current_directImpact': current_directImpact, 
    'current_impact': current_impact, 
    'current_incidentChange': current_incidentChange, 
    'current_means': current_means, 
    'current_severityOfImpact': current_severityOfImpact, 
    'current_source': current_source, 
    'current_victim': current_victim, 
    'current_victimSector': current_victimSector}
    # return HttpResponse(template.render(context))
    return render(request, 'CPSIDapp/incidentDetail.html', context)

def test(request):
    return render(request, 'CPSIDapp/test.html',None)
