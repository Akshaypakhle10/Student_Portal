from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import profile

# Create your views here.
def home(request):
	context = {}
	template = 'home.html'
	return render(request,template,context)
	print ('Im in home')

def about(request):
	context = {}
	model = profile
	template = 'about.html'
	return render(request,template,context)
	print ('Im in BOUT')


@login_required
def userProfile(request):
	user = request.user
	context = {'user': user}
	template = 'profile.html'
	return render(request,template,context)
	print ('Im in USEP')
