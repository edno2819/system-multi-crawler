# Generated by Django 4.2.1 on 2023-07-18 01:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0004_alter_product_uri_picturemetadata"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="color",
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]