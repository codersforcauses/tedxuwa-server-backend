from django.shortcuts import render
from django.http.response import HttpResponse
from django.conf import settings
from django.views.generic.base import TemplateView
from ratelimit.mixins import RatelimitMixin
from ratelimit.utils import is_ratelimited
from ratelimit.decorators import ratelimit

# Create your views here.


class ReactAppView(TemplateView, RatelimitMixin):
    template_name = settings.FRONTEND_ENTRY_POINT
    ratelimit_group = "main"
    ratelimit_key = "ip"
    ratelimit_rate = "0/s"
    ratelimit_block = True


def rate_limited_react_view(request):
    return render(request, settings.FRONTEND_ENTRY_POINT)
