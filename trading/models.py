from django.db import models

class Trade(models.Model):
    symbol = models.CharField(max_length=10)
    entry_price = models.FloatField()
    exit_price = models.FloatField(null=True, blank=True)
    quantity = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.symbol} - {self.entry_price}"
