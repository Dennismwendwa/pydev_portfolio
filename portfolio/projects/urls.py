
from django.urls import path
from . import views


urlpatterns = [
	path('', views.projects, name="projects"),
	path('portfolio-details', views.portfolio_details, name="portfolio_details"),
	path('contact', views.contact, name="contact"),
]


