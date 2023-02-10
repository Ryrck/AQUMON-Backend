from django.db import models
from django.contrib import admin

# Create your models here.
class Stock(models.Model):
    stock_symbol = models.CharField(max_length = 10)
    stock_price = models.DecimalField(max_digits=20, decimal_places=2)
    stock_date = models.DateTimeField()

    def __str__(self):
        return self.stock_symbol

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Stock._meta.fields]
    fields = ['stock_price']
    search_fields = ['stock_symbol']