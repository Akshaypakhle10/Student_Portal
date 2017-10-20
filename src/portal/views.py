from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def portal(request):
	user = request.user
	context = {'user': user}
	template = 'portal.html'
	return render(request,template,context)
	print ('Im in portal')
