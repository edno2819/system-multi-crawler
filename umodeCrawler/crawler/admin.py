from django.contrib import admin
from crawler.models import *


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    class Meta:
        model = Site


@admin.register(Crawler)
class CrawlerAdmin(admin.ModelAdmin):
    readonly_fields=('site_id', "started_at", "finished_at", "products", "categories", "errors")

    list_per_page = 20
    search_fields = ["site_id"]
    list_filter = [
        "site_id",
    ]
    list_display = [
        "site_id",
        "started_at",
        "products",
    ]
    class Meta:
        model = Crawler

