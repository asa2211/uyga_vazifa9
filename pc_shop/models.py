from datetime import datetime

from django.db import models


class CategoryModel(models.Model):
    category_name = models.CharField(default='', max_length=100)

    def __str__(self):
        return self.category_name

    class Meta:
        db_table = "category"


class PCModel(models.Model):
    pc_name = models.CharField(default='', max_length=30)
    cpu = models.CharField(default='', max_length=30)
    gpu = models.CharField(default='', max_length=40)
    rom = models.CharField(default='', max_length=15)
    ram = models.CharField(default='', max_length=15)
    added_at = models.DateTimeField(datetime.now)
    price = models.CharField(max_length=255)
    category_id = models.ForeignKey(on_delete=models.CASCADE, to=CategoryModel)

    def __str__(self):
        return self.pc_name

    class Meta:
        db_table = "pc_shop"
