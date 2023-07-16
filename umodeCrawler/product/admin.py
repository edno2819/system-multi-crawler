from django.contrib import admin
from .models import *


class ProductSizesInline(admin.StackedInline):
    model = ProductSizes
    extra = 1


class ProductPriceInline(admin.StackedInline):
    model = ProductPrice
    extra = 1


class ProductAttributesInline(admin.StackedInline):
    model = ProductAttributes
    extra = 1


class PictureMetadataInline(admin.StackedInline):
    model = PictureMetadata
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "site_id", "sku", "color", "uri", "crawler_date"]
    inlines = [
        ProductSizesInline,
        ProductPriceInline,
        ProductAttributesInline,
        PictureMetadataInline,
    ]
    list_filter = ["name", "color"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_filter = ["name"]


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "category_id"]
    list_filter = ["name", "category_id__name"]


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ["id", "nome"]
    list_filter = ["nome"]
