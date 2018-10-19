from django.contrib.sitemaps import Sitemap
from django.utils.text import slugify
from events.models import Event

# https://docs.djangoproject.com/en/2.1/ref/contrib/sitemaps/


class EventSitemap(Sitemap):
    def items(self):
        return Event.objects.all()

    def lastmod(self, obj):
        return obj.updated

    def location(self, obj):
        return f"/events/{obj.id}/{slugify(obj.name, allow_unicode=True)}"


class StaticPagesSitemap(Sitemap):
    # return static pages (non model links)
    def items(self):
        # these paths are front end paths. They don't exist here in the server
        return [
            "/",
            "/sponsors",
            "/contact",
            "/events",
            "/about"
        ]

    def location(self, path):
        return path


sitemaps = {
    "events": EventSitemap,
    "static_pages": StaticPagesSitemap
}
