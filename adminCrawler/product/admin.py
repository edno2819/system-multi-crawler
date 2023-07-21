from django.contrib import admin
from .models import *
from django.utils.html import format_html


class ProductSizesInline(admin.StackedInline):
    readonly_fields=('crawled_at', 'size', 'stock')
    model = ProductSizes
    extra = 1


class ProductPriceInline(admin.StackedInline):
    readonly_fields=('crawled_at', 'price', 'promotional_price')
    model = ProductPrice
    extra = 1


class ProductAttributesInline(admin.StackedInline):
    model = ProductAttributes
    extra = 1


class PictureMetadataInline(admin.StackedInline):
    readonly_fields=('picture_url', 'metadata')
    model = PictureMetadata
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields=('site_id', 'crawler_date')
    list_display = ["name", "site_id", "color", "uri", "crawler_date", "display_picture"]
    inlines = [
        ProductSizesInline,
        ProductPriceInline,
        ProductAttributesInline,
        PictureMetadataInline,
    ]
    list_filter = ["name", "color"]
    
    def display_picture(self, obj):
        picture = obj.picturemetadata_set.first()
        if picture:
            return format_html('<img src="{}" width="60" height="60" />', picture.picture_url)
        return 'No Image'
    display_picture.short_description = 'Picture'


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
