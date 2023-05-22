from django.shortcuts import render
from . models import Projets
# Create your views here.

def projects(request):

	project = Projets.objects.all()
	print(project)
	return render(request, "projects/home.html", { "project": project,})
