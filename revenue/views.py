from rest_framework import viewsets
from .models import RevenueStatistic
from .serializers import RevenueListSerializer
from django.db.models import Sum


class RevenueStatisticViewSet(viewsets.ModelViewSet):
    queryset = RevenueStatistic.objects.values("date", "name") \
        .annotate(revenue_sum=Sum('revenue')) \
        .annotate(spend_sum=Sum('spend__spend')) \
        .annotate(impressions_sum=Sum('spend__impressions')) \
        .annotate(clicks_sum=Sum('spend__clicks')) \
        .annotate(conversion_sum=Sum('spend__conversion'))
    serializer_class = RevenueListSerializer
    basename = 'revenue-statistic'

