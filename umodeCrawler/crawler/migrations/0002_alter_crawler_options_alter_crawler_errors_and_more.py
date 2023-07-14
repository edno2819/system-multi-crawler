# Generated by Django 4.2.1 on 2023-07-14 21:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("crawler", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="crawler",
            options={"verbose_name": "Crawler Execução"},
        ),
        migrations.AlterField(
            model_name="crawler",
            name="errors",
            field=models.JSONField(blank=True, default=[], null=True),
        ),
        migrations.AlterField(
            model_name="crawler",
            name="finished_at",
            field=models.DateTimeField(),
        ),
        migrations.AlterModelTable(
            name="crawler",
            table="crawler",
        ),
        migrations.AlterModelTable(
            name="site",
            table="site",
        ),
    ]
