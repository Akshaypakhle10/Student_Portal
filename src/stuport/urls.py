"""stuport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from profiles import views as profile_views
from contact import views as contact_views
from portal import views as portal_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', profile_views.home, name='home'),
    url(r'^about/$', profile_views.about, name='about'),
    url(r'^profile/$', profile_views.userProfile, name='profile'),
    url(r'^profile/edit/$', profile_views.edit_profile, name='edit_profile'),
    url(r'^contact/$', contact_views.contact, name='contact'),
    url(r'^portal/$', portal_views.portal, name='portal'),
    url(r'^assignments/$', portal_views.assignments, name='assignments'),
    url(r'^lab_manuals/$', portal_views.lab_manuals, name='lab_manuals'),
    url(r'^reference_material/$', portal_views.reference_material, name='reference_material'),
    url(r'^sample_papers/$', portal_views.sample_papers, name='sample_papers'),
    url(r'^timetable/$', portal_views.timetable, name='timetable'),
    url(r'^accounts/', include('allauth.urls')),

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)	