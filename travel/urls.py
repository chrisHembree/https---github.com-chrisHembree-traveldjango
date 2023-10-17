from django.urls import path
from travel import views as travel_views

urlpatterns = [
    path('create/', travel_views.CreateDestinationDetailsView.as_view(), name='create'),
    
]