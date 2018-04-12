from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class IndexView(TemplateView):
    """
    The origin of all front end views start here
    """
    template_name = "react_base.html"
