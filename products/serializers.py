from rest_framework import serializers

from products.models import Products


class Products_serializer(serializers.ModelSerializer):
    prd_owner = serializers.SerializerMethodField()

    class Meta:
        model = Products
        fields = '__all__'

    def get_prd_owner(self, obj):
        return obj.prd_owner.username
