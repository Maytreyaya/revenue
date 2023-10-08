from rest_framework import serializers
from revenue.models import RevenueStatistic


class RevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueStatistic
        fields = ("__all__")


class RevenueListSerializer(RevenueSerializer):

    revenue_sum = serializers.IntegerField(read_only=True)
    spend_sum = serializers.IntegerField(read_only=True)
    impressions_sum = serializers.IntegerField(read_only=True)
    clicks_sum = serializers.IntegerField(read_only=True)
    conversion_sum = serializers.IntegerField(read_only=True)

    class Meta:
        model = RevenueStatistic
        fields = (
            "date",
            "revenue_sum",
            "spend_sum",
            "impressions_sum",
            "clicks_sum",
            "conversion_sum",
        )
