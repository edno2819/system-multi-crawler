from django.contrib import admin
from crawler.models import *
import requests


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    actions = ['enviar_requisicao_post']
    list_display = [
        "name",
        "url",
    ]

    class Meta:
        model = Site
        
    def enviar_requisicao_post(self, request, queryset):
        sites = list(queryset.values_list('name', flat=True))
        
        url = 'http://server:5000/crawler'
        response = requests.post(url, json={"sites": sites})

        if response.status_code == 200:
            self.message_user(request, "Crawler iniciado com sucesso!")
        else:
            self.message_user(request, "Falha ao iniciar o crawler!")

    enviar_requisicao_post.short_description = "Executar Crawler"


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

