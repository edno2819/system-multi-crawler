# Generated by Django 4.2.1 on 2023-07-15 14:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("crawler", "0002_alter_crawler_options_alter_crawler_errors_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="crawler",
            options={
                "verbose_name": "Crawler Execução",
                "verbose_name_plural": "Crawler Execuções",
            },
        ),
        migrations.AlterField(
            model_name="crawler",
            name="errors",
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]
