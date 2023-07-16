# Generated by Django 4.2.1 on 2023-07-16 22:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="crawler_date",
            field=models.DateField(max_length=255),
        ),
        migrations.AlterField(
            model_name="product",
            name="metadata",
            field=models.JSONField(blank=True, max_length=1024, null=True),
        ),
    ]
