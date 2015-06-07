from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.forms.models import modelformset_factory
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.views.generic.base import TemplateView
from django.contrib import messages
from incidents.models import IncidentType
# from incidents.forms import SubmitIncidentFor
from django.views.generic.edit import FormView
# from incidents.models import I


# class SubmitIncidentView(FormView):
# template_name = 'incidents/incidents_form.html'
#     form_class = SubmitIncidentForm
#     success_url = 'incidents/thanks/'
#
#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         form.submit_incident()
#         return super(SubmitIncidentView, self).form_valid(form)

# def SubmitIncidentView(request):
#     template_name = 'incidents/incidents_form.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(IncidentPageView, self).get_context_data(**kwargs)
#         messages.info(self.request, 'Welcome to Tshwane Connect, a webapp by SWNE')
#         return context


class IncidentPageView(TemplateView):
    template_name = 'incidents/incidents.html'

    def get_context_data(self, **kwargs):
        context = super(IncidentPageView, self).get_context_data(**kwargs)
        messages.info(self.request, 'Alert: Power Outage in Mamelodi East')
        return context

class SubmitIncidentPageView(TemplateView):
    template_name = 'incidents/incidents_form.html'

    def get_context_data(self, **kwargs):
        context = super(SubmitIncidentPageView, self).get_context_data(**kwargs)
        # messages.info(self.request, 'Alert: Power Outage in Mamelodi East')
        return context


# def manage_authors(request):
# AuthorFormSet = modelformset_factory(Incident, fields=('name', 'incident_type', 'time'))
# if request.method == 'POST':
#         formset = AuthorFormSet(request.POST, request.FILES)
#         if formset.is_valid():
#             formset.save()
#             # do something.
#     else:
#         formset = AuthorFormSet()
#     return render_to_response("/incidents/incidents.html", {
#         "formset": formset,
#     })




# from .forms import ContactForm, FilesForm, ContactFormSet


