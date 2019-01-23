from django.shortcuts import render
from .models import Person
from .models import Project
# Create your views here.

def site(request):
	
	person = Person.objects.all()
	project = Project.objects.all()
	context = {'person': person, 'project':project}
	return render(request, 'base.html', context)