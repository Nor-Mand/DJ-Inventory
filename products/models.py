from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product_category'
        verbose_name_plural = 'Product Category'


class ProductTemplate(models.Model):
    PRODUCT_TYPE = {
        "product": "Storable",
        "consu": "Consumable",
        "services": "Services"
    }

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=200, choices=PRODUCT_TYPE)
    cost = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField(max_length=350)
    ref = models.CharField(max_length=50)
    category_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product_template'
        verbose_name_plural = 'Product Template'


