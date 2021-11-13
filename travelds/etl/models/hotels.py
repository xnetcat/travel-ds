from django.db import models


class HotelsListing(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=45)
    country_name = models.CharField(max_length=2)
    lat = models.FloatField()
    lon = models.FloatField()
    room_and_property_type = models.CharField(max_length=45)
    num_rooms = models.IntegerField(null=True)
    url = models.CharField(max_length=255)
    hotel_chain = models.CharField(max_length=45)
    wiki_entity = models.CharField(max_length=10)
    hotel_stars = models.IntegerField(null=True)
    is_multiple = models.BooleanField(null=True)
    is_tracked = models.BooleanField(null=True)
    first_seen = models.DateField()
    last_seen = models.DateField()
    open_on = models.DateField()

    class Meta:
        app_label = "hotels"
        db_table = "hotels_listing"


class HotelsPrice(models.Model):
    listing = models.ForeignKey(HotelsListing, on_delete=models.DO_NOTHING)
    ref_period = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()
    rate_with_service_fee = models.FloatField()
    currency = models.CharField(max_length=3)
    available = models.BooleanField()
    is_bookable = models.BooleanField(null=True)
    room_count = models.IntegerField(null=True)

    class Meta:
        app_label = "hotels"
        db_table = "hotels_price"
        unique_together = ("listing", "start_date", "end_date", "ref_period")