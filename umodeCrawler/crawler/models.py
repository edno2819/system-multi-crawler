from django.db import models
import datetime


class Site(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False, blank=True)
    url = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'site'
        
    def __str__(self):
        return self.name

class Crawler(models.Model):
    id = models.AutoField(primary_key=True)
    site_id = models.ForeignKey(
        Site,
        on_delete=models.DO_NOTHING,
        blank=False,
        null=False,
    )
    started_at = models.DateTimeField(default=datetime.datetime.now)
    finished_at = models.DateTimeField(null=False, blank=False)
    categories = models.IntegerField(default=0)
    products = models.IntegerField(default=0)
    errors = models.JSONField(default=list, null=True, blank=True)  
    
    class Meta:
        db_table = 'crawler'
        verbose_name = "Crawler Execução"
        verbose_name_plural = "Crawler Execuções"

        
    def __str__(self):
        return f'{self.site_id} - {self.started_at}'