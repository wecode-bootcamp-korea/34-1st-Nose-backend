from django.db import models

class Product(models.Model):
    name        = models.CharField(max_length=128)
    price       = models.DecimalField(max_digits=8, decimal_places=2)
    category    = models.ForeignKey("Category", on_delete=models.CASCADE, null=True)
    fragrances  = models.ManyToManyField("Fragrance", db_table="products_fragrances")
    ingredients = models.ManyToManyField("Ingredient", db_table="products_ingredients")
    tags        = models.ManyToManyField("Tag", db_table="products_tags")

    class Meta:
        db_table = "products"

class ThumbNailImage(models.Model):
    thumb_nail_img_url = models.CharField(max_length=300)
    product            = models.ForeignKey("Product", on_delete=models.CASCADE)

    class Meta:
        db_table = "thumb_nail_images"

class MainImage(models.Model):
    main_page_img_url = models.CharField(max_length=300)
    product           = models.ForeignKey("Product", on_delete=models.CASCADE)

    class Meta:
        db_table = "main_images"

class DetailImage(models.Model):
    detail_page_img_url = models.CharField(max_length=300)
    product             = models.ForeignKey("Product", on_delete=models.CASCADE)

    class Meta:
        db_table = "detail_images"

class Category(models.Model):
    name    = models.CharField(max_length=45)

    class Meta:
        db_table = "categories"

class Fragrance(models.Model) :
    name = models.CharField(max_length=45)
    
    class Meta:
        db_table = "fragrances"

class Ingredient(models.Model) :
    name = models.CharField(max_length=45)

    class Meta:
        db_table = "ingredients"

class Tag(models.Model):
    name    = models.CharField(max_length=45)

    class Meta:
        db_table = "tags"