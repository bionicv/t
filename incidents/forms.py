from django import forms
from incidents.models import Incident
from django.core.exceptions import ValidationError


# class SubmitIncidentForm(forms.ModelForm):
#     class Meta:
#         model = Incident
#
#     def __init__(self, *args, **kwargs):
#         if kwargs.get('instance'):
#             name = kwargs['instance'].name
#             time = kwargs['instance'].time
#             description = kwargs['instance'].description
#
#         return super(SubmitIncidentForm, self).__init__(*args, **kwargs)
#
#     def submit_incident(self):
#         # Submit incident
#         pass