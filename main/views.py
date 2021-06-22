from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.conf import settings
from django.views.generic.base import TemplateView
from django.contrib.admin.views.decorators import staff_member_required
from  django.views.decorators.cache import cache_control
from ratelimit.mixins import RatelimitMixin
from ratelimit.utils import is_ratelimited
from ratelimit.decorators import ratelimit
from rest_framework.generics import ListAPIView
from constance import config
import os

from .models import Sponsor, ForwardLink
from .serializers import SponsorSerializer

# Create your views here.

# DEPRECATED


class ReactAppView(TemplateView, RatelimitMixin):
    template_name = settings.FRONTEND_ENTRY_POINT
    ratelimit_group = "main"
    ratelimit_key = "ip"
    ratelimit_rate = "0/s"
    ratelimit_block = True

@cache_control(max_age=3600)
def react_view(request):
    return render(request, settings.FRONTEND_ENTRY_POINT)


def robotstxt_view(request):
    # tell scrapers not to scrape admin
    content = """
User-agent: *
Disallow: /admin/
"""
    return HttpResponse(content, content_type="text/plain")


@staff_member_required
def download_db(request):
    file_path = settings.DATABASES["default"]["NAME"]
    with open(file_path, 'rb') as fh:
        response = HttpResponse(
            fh.read(), content_type="application/x-sqlite3")
        response['Content-Disposition'] = 'inline; filename=' + \
            os.path.basename(file_path)
        return response


class SponsorViewSet(ListAPIView):
    # only allow listing and fetching single
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer


def redirect_short_link(request, path):
    # redirect and send event to google analytics
    try:
        url_obj = ForwardLink.objects.get(path=path)
        url = url_obj.link
        title = url_obj.title
    except ForwardLink.DoesNotExist:
        url = "tedxuwa.com"  # default
        title = "TEDxUWA"
    return render(request,
                  "main/redirect.html",
                  {
                      "redirect_url": url,
                      "title": title}
                  )


def reach_data(request):
    return JsonResponse({
        'followers': config.REACH_FOLLOWERS,
        'speakers': config.REACH_SPEAKERS,
        'subscribers': config.REACH_SUBSCRIBERS
    })
