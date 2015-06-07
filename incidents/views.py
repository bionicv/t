from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.forms.models import modelformset_factory
from django.shortcuts import render_to_response
from incidents.models import Incident

def manage_authors(request):
    AuthorFormSet = modelformset_factory(Incident, fields=('name', 'incident_type','time'))
    if request.method == 'POST':
        formset = AuthorFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            # do something.
    else:
        formset = AuthorFormSet()
    return render_to_response("/incidents/incidents.html", {
        "formset": formset,
    })

from django.views.generic.base import TemplateView
from django.contrib import messages

#from .forms import ContactForm, FilesForm, ContactFormSet


class IncidentPageView(TemplateView):
    template_name = 'incidents/incidents.html'

    def get_context_data(self, **kwargs):
        context = super(IncidentPageView, self).get_context_data(**kwargs)
        messages.info(self.request, 'Welcome to Tshwane Connect, a webapp by SWNE')
        return context
