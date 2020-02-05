from django.db import models

class Rooms(models.Model):
    room_id = models.IntegerField(primary_key=True, unique=True, editable=False)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    coordinates = models.CharField(max_length=200)
    # May need adjustments for array fields. blank=True allows for empty fields
    players = ArrayField(models.CharField(), blank=True)
    items = ArrayField(models.CharField(), blank=True)
    exits = ArrayField(models.CharField(), blank=True)
    cooldown = models.IntegerField(editable=False, blank=False)
    errors = ArrayField(models.CharField(), blank=True)
    messages = ArrayField(models.CharField(), blank=True)