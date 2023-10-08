from django.db import models
from spend.models import SpendStatistic


class RevenueStatistic(models.Model):
    name = models.CharField(max_length=255)
    spend = models.ForeignKey('spend.SpendStatistic', on_delete=models.SET_NULL, null=True, related_name="spends")
    date = models.DateField()
    revenue = models.DecimalField(max_digits=9, decimal_places=2, default=0)

    def __str__(self):
        return f"Revenue {self.name}({self.revenue}) created on {self.date}"

