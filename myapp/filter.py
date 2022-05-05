import django_filters
from django_filters import filters

from .models import VehicleModel


class SearchFilter(django_filters.FilterSet):
    from_location = filters.CharFilter(field_name="from_location", lookup_expr='icontains')
    to_location = filters.CharFilter(field_name="to_location", lookup_expr='icontains')
    # provider = filters.CharFilter(field_name="provider", lookup_expr='icontains')
    # price = filters.CharFilter(field_name="price",)
    class Meta:
        model = VehicleModel
        fields = []

    