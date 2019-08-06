"""root URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include, re_path
from django.conf import settings
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter

from events.views import EventViewSet, SpeakerViewSet, SpeakerListViewSet, TalkViewSet
from tedxuwa_user.views import CommitteeListView
from main.views import ReactAppView, react_view, robotstxt_view, SponsorViewSet, download_db
from root.sitemaps import sitemaps

admin.site.site_header = "TEDxUWA Administration"

router = DefaultRouter()
router.register(r'^events', EventViewSet)
router.register(r'^talks', TalkViewSet)

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url="{}favicon.ico".format(
        settings.STATIC_URL), permanent=True)),
    path('admin/downloaddb/', download_db),
    path('admin/', admin.site.urls),
    # api views
    path('api/', include(router.urls)),
    path('api/committee/', CommitteeListView.as_view()),
    path('api/events/<int:event_id>/speakers/', SpeakerViewSet.as_view()),
    path('api/sponsors/', SponsorViewSet.as_view()),
    path('api/speakers/', SpeakerListViewSet.as_view()),
    # others
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', robotstxt_view),
    # https://medium.com/@nicholaskajoh/heres-a-dead-simple-react-django-setup-for-your-next-project-c0b0036663c6
    # re_path('.*', ReactAppView.as_view()),
    re_path('.*', react_view),
]
