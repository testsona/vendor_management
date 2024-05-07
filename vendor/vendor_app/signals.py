from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg
from vendor_app.models import PurchaseOrder
from django.db.models import F
from django.utils import timezone


@receiver(post_save, sender=PurchaseOrder)
def update_vendor_performance(sender, instance, **kwargs):
    if instance.status == "completed" and instance.delivered_data is None:
        instance.delivered_data = timezone.now()
        instance.save()

    # Update On-Time Delivery Rate
    completed_orders = PurchaseOrder.objects.filter(
        vendor=instance.vendor, status="completed"
    )
    on_time_deliveries = completed_orders.filter(delivery_date__gte=F("delivered_data"))
    on_time_delivery_rate = on_time_deliveries.count() / completed_orders.count()
    instance.vendor.on_time_delivery_rate = (
        on_time_delivery_rate if on_time_delivery_rate else 0
    )

    # Update Quality Rating Average
    completed_orders_with_rating = completed_orders.exclude(quality_rating__isnull=True)
    quality_rating_avg = (
        completed_orders_with_rating.aggregate(Avg("quality_rating"))[
            "quality_rating__avg"
        ]
        or 0
    )
    instance.vendor.quality_rating_avg = quality_rating_avg if quality_rating_avg else 0
    instance.vendor.save()


@receiver(post_save, sender=PurchaseOrder)
def update_response_time(sender, instance, **kwargs):
    # Update Average Response Time
    response_times = PurchaseOrder.objects.filter(
        vendor=instance.vendor, acknowledgment_date__isnull=False
    ).values_list("acknowledgment_date", "issue_date")
    average_response_time = sum(
        (ack_date - issue_date).total_seconds()
        for ack_date, issue_date in response_times
    )  # / len(response_times)
    if average_response_time < 0:
        average_response_time = 0
    if response_times:
        average_response_time = average_response_time / len(response_times)
    else:
        average_response_time = 0
    instance.vendor.average_response_time = average_response_time
    instance.vendor.save()


@receiver(post_save, sender=PurchaseOrder)
def update_fulfillment_rate(sender, instance, **kwargs):
    # Update Fulfillment Rate
    fulfilled_orders = PurchaseOrder.objects.filter(
        vendor=instance.vendor, status="completed"
    )
    fulfillment_rate = (
        fulfilled_orders.count()
        / PurchaseOrder.objects.filter(vendor=instance.vendor).count()
    )
    instance.vendor.fulfillment_rate = fulfillment_rate
    instance.vendor.save()
