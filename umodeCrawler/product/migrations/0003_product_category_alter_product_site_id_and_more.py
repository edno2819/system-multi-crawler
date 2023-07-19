# Generated by Django 4.2.1 on 2023-07-16 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("crawler", "0005_alter_crawler_options"),
        ("product", "0002_alter_product_crawler_date_alter_product_metadata"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                blank=True,
                db_column="categories",
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="product.category",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="site_id",
            field=models.ForeignKey(
                db_column="site_id",
                on_delete=django.db.models.deletion.CASCADE,
                to="crawler.site",
            ),
        ),
        migrations.AlterField(
            model_name="subcategory",
            name="category_id",
            field=models.ForeignKey(
                db_column="categories",
                on_delete=django.db.models.deletion.CASCADE,
                to="product.category",
            ),
        ),
        migrations.AlterModelTable(
            name="category",
            table="categories",
        ),
        migrations.AlterModelTable(
            name="subcategory",
            table="sub_categories",
        ),
    ]