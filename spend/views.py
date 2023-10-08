from django.db.models import Sum
from rest_framework import viewsets

from spend.models import SpendStatistic
from spend.serializers import SpendListSerializer


class SpendStatisticViewSet(viewsets.ModelViewSet):
    queryset = SpendStatistic.objects.values("date", "name") \
        .annotate(spend_sum=Sum('spend')) \
        .annotate(impressions_sum=Sum('impressions')) \
        .annotate(clicks_sum=Sum('clicks')) \
        .annotate(conversion_sum=Sum('conversion')) \
        .annotate(revenue_sum=Sum('spends__revenue'))
    serializer_class = SpendListSerializer
    basename = 'spend-statistic'
