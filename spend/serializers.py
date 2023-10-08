from rest_framework import serializers
from revenue.models import SpendStatistic


class SpendSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpendStatistic
        fields = "__all__"


class SpendListSerializer(SpendSerializer):

    spend_sum = serializers.IntegerField(read_only=True)
    impressions_sum = serializers.IntegerField(read_only=True)
    clicks_sum = serializers.IntegerField(read_only=True)
    conversion_sum = serializers.IntegerField(read_only=True)
    revenue_sum = serializers.IntegerField(read_only=True)

    class Meta:
        model = SpendStatistic
        fields = (
            "date",
            "spend_sum",
            "impressions_sum",
            "clicks_sum",
            "conversion_sum",
            "revenue_sum",
        )
