from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    rating = models.FloatField()
    room_type = models.CharField(max_length=50)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_rooms = models.IntegerField()
    wifi_available = models.BooleanField(default=True)
    pool_available = models.BooleanField(default=False)
    gym_available = models.BooleanField(default=False)
    Laundry_facilities = models.BooleanField(default=False)
    Parking = models.BooleanField(default=False)
    Restaurant = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images',null=True)
    def __str__(self):
        return self.name

# class HotelImage(models.Model):
#     hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
#     # image = models.ImageField(upload_to='')
#
#     def __str__(self):
#         return f"Image of {self.hotel.name}"