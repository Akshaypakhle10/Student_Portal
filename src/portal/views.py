from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Assignments,Lab_Manuals,Reference_Material,Sample_Papers,Timetable
# Create your views here.
@login_required
def portal(request):
	context = {}
	template = 'portal.html'
	return render(request,template,context)

def assignments(request):
	model = Assignments
	file = Assignments.objects.all()
	context = {'file': file}
	template = 'assignments.html'
	context_object_name = 'obj'

    
	return render(request,template,context)

def lab_manuals(request):
	model = Lab_Manuals
	file = Lab_Manuals.objects.all()
	context = {'file': file}
	template = 'lab_manuals.html'
	context_object_name = 'obj'

    
	return render(request,template,context)

def reference_material(request):
	model = Reference_Material
	file = Reference_Material.objects.all()
	context = {'file': file}
	template = 'reference_material.html'
	context_object_name = 'obj'

    
	return render(request,template,context)

def timetable(request):
	model = Timetable
	file = Timetable.objects.all()
	context = {'file': file}
	template = 'timetable.html'
	context_object_name = 'obj'

    
	return render(request,template,context)

def sample_papers(request):
	model = Sample_Papers
	file = Sample_Papers.objects.all()
	context = {'file': file}
	template = 'sample_papers.html'
	context_object_name = 'obj'

    
	return render(request,template,context)

