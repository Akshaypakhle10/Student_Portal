from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Profile
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('alltracks')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def about(request):
    context = {}
    template = 'about.html'
    return render(request,template,context)

@login_required
def userProfile(request):
	user = request.user
	context = {'user':user}
	template = 'profile.html'
	return render(request,template,context)


def logout_view(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'Successfully Logged Out')
    return HttpResponseRedirect('/login/')

def home(request):
    context = {}
    template = 'home.html'
    return render(request,template,context)

def edit_profile(request):
    return render('edit')