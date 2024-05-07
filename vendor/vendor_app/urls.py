# vendor_app/urls.py
from django.urls import path
from vendor_app.views import (
    VendorListCreateView,
    VendorRetrieveUpdateDeleteView,
    PurchaseOrderListCreateView,
    PurchaseOrderRetrieveUpdateDeleteView,
    VendorPerformanceView,
    AcknowledgeUpdateView,
)

urlpatterns = [
    # Endpoint for listing and creating vendors
    path("vendors/", VendorListCreateView.as_view(), name="vendor-list-create"),
    # Endpoint for retrieving, updating, or deleting a specific vendor
    path(
        "vendors/<int:pk>/",
        VendorRetrieveUpdateDeleteView.as_view(),
        name="vendor-retrieve-update-delete",
    ),
    # Endpoint for listing and creating purchase orders
    path(
        "purchase_orders/",
        PurchaseOrderListCreateView.as_view(),
        name="purchase-order-list-create",
    ),
    # Endpoint for retrieving, updating, or deleting a specific purchase order
    path(
        "purchase_orders/<int:pk>/",
        PurchaseOrderRetrieveUpdateDeleteView.as_view(),
        name="purchase-order-retrieve-update-delete",
    ),
    # Endpoint for viewing vendor performance metrics
    path(
        "vendors/<int:pk>/performance/",
        VendorPerformanceView.as_view(),
        name="vendor-performance",
    ),
    # Endpoint for acknowledging and updating a purchase order status
    path(
        "purchase_orders/<int:pk>/acknowledge/",
        AcknowledgeUpdateView.as_view(),
        name="acknowledge-purchase-order",
    ),
]
