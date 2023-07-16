from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False, blank=False, unique=True)

    class Meta:
        db_table = "categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False, blank=True)
    site_id = models.ForeignKey(
        "crawler.Site",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        db_column="site_id",
    )
    sku = models.CharField(max_length=512)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        db_column="categories",
    )
    color = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    color = models.CharField(max_length=32)
    uri = models.URLField(max_length=255)
    crawler_date = models.DateField(max_length=255)
    metadata = models.JSONField(max_length=1024, blank=True, null=True)

    class Meta:
        db_table = "products"

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False, blank=False, unique=True)
    category_id = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        db_column="categories",
    )

    class Meta:
        db_table = "sub_categories"

    def __str__(self):
        return f"{self.category_id} - {self.name}"


class ProductSizes(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        db_column="product_id",
    )
    size = models.CharField(max_length=64)
    stock = models.IntegerField(null=True, blank=True)
    crawled_at = models.DateField(null=False, blank=False)

    class Meta:
        db_table = "products_sizes"

    def __str__(self):
        return f"{self.product_id} - {self.size} - {self.stock} - {self.crawled_at}"


class ProductPrice(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(
        Product,
        on_delete=models.DO_NOTHING,
        blank=False,
        null=False,
        db_column="product_id",
    )
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    promotional_price = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    crawled_at = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "products_price"

    def __str__(self):
        return self.product_id


class Attribute(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)

    class Meta:
        db_table = "attribute"

    def __str__(self):
        return self.nome


class ProductAttributes(models.Model):
    id = models.AutoField(primary_key=True)
    attribute_id = models.ForeignKey(
        Attribute,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        db_column="attribute",
    )
    product_id = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        db_column="product_id",
    )
    score = models.FloatField(null=False, blank=True)

    class Meta:
        db_table = "products_attributes"

    def __str__(self):
        return self.attribute_id


class PictureMetadata(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        db_column="product_id",
    )
    picture_url = models.URLField(max_length=512)
    metadata = models.JSONField(max_length=1024, blank=True, null=True)

    class Meta:
        db_table = "pictures_metadata"

    def __str__(self):
        return self.product_id
