from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('deals/',views.deals,name="deals"),
    path('reservation/',views.reservation,name="reservation")
    # Add more URL patterns as needed
]