from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import CreateDestinationDetailsForm

class CreateDestinationDetailsView(FormView):
    form_class = CreateDestinationDetailsForm
    template_name = "traveldjango/templates/createdestinationdetails.html" 
    success_url = reverse_lazy('travel:create')


