from django.urls import path
from mainapp.views import SchoolView


urlpatterns = [
    path('create_school/', SchoolView.as_view()),
]