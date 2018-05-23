from django.shortcuts import render
from django.conf import settings
from django.views.generic.base import TemplateView

# Create your views here.


class ReactAppView(TemplateView):
    template_name = settings.FRONTEND_ENTRY_POINT
