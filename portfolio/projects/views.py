from django.shortcuts import render, redirect
from . models import Projets
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


from .forms import ContactForm

# Create your views here.

def projects(request):

	project = Projets.objects.all()
	
	return render(request, "projects/index.html", { "project": project,})

def portfolio_details(request):


	return render(request, "projects/portfolio-details.html", {})

def contact(request):

	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data["email"]
			subject = form.cleaned_data["subject"]
			message = form.cleaned_data["message"]

			email_message = f"Name: {name}\nEmail: {email}\nSubject: {subject}\n\n{message}"
		
			#Sending the email
			send_mail(
				subject = "New contact form subnission",
				message = email_message,
				from_email = email,
				recipient_list=['dennismusembi2@gmail.com', 'dennissoftware3@gmail.com', ],
				fail_silently=False,
				)
			messages.success(request, "Your message was send successfully. We will get in tourch soon")
#			return redirect("projects")
			return redirect("projects")
	else:
		form = ContactForm()

	return render(request, "projects/index.html", {})
