from django.urls import path
from .views import CreateDestinationDetailsView

app_name = 'travel'

urlpatterns = [
    path('', CreateDestinationDetailsView.as_view(), name='create'),
    
]