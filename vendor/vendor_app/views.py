from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from vendor_app.models import Vendor, PurchaseOrder
from django.utils import timezone
from rest_framework.generics import UpdateAPIView
from vendor_app.serializers import (
    VendorSerializer,
    PurchaseOrderSerializer,
    AcknowledgeSerializer,
)

# Create your views here.


class VendorListCreateView(generics.ListCreateAPIView):
    """API view for listing and creating vendors."""

    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """API view for listing and creating vendors."""

    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    """API view for listing and creating purchase orders."""

    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


class PurchaseOrderRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """API view for retrieving, updating, or deleting a specific purchase order."""

    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


class VendorPerformanceView(generics.RetrieveAPIView):
    """API view for retrieving vendor performance metrics."""

    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(
            {
                "on_time_delivery_rate": serializer.data["on_time_delivery_rate"],
                "quality_rating_avg": serializer.data["quality_rating_avg"],
                "average_response_time": serializer.data["average_response_time"],
                "fulfillment_rate": serializer.data["fulfillment_rate"],
            }
        )


class AcknowledgeUpdateView(UpdateAPIView):
    """API view for acknowledging and updating a purchase order."""

    queryset = PurchaseOrder.objects.all()
    serializer_class = AcknowledgeSerializer

    def perform_update(self, serializer):
        serializer.validated_data["acknowledgment_date"] = timezone.now()
        super().perform_update(serializer)
        return Response(serializer.data)
