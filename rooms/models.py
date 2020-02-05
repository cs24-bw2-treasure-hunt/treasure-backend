from django.db import models
from django.contrib.postgres.fields import ArrayField

class Room(models.Model):
    room_id = models.IntegerField(primary_key=True, unique=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    coordinates = models.CharField(max_length=32)
    players = models.CharField(max_length=255, blank=True)
    items = models.CharField(max_length=255, blank=True)
    exits = models.CharField(max_length=255)
    cooldown = models.IntegerField(blank=True, editable=False)
    errors = models.CharField(max_length=255, blank=True)
    messages = models.CharField(max_length=500, blank=True)

    # May need adjustments for array fields. blank=True allows for empty fields. DOES NOT WORK WITH SQL
    # players = ArrayField(models.CharField(max_length=255), default=list)
    # items = ArrayField(models.CharField(max_length=255), default=list)
    # exits = ArrayField(models.CharField(max_length=255), default=list)
    # cooldown = models.IntegerField(editable=False)
    # errors = ArrayField(models.CharField(max_length=255), default=list)
    # messages = ArrayField(models.CharField(max_length=255), default=list)

class Inventory(models.Model):
    name = models.CharField(max_length=20, blank=True)
    cooldown = models.IntegerField(blank=True)
    encumbrance = models.IntegerField(default=0, blank=True)
    strength = models.IntegerField(default=10, blank=True)
    speed = models.IntegerField(default=10, blank=True)
    gold = models.IntegerField(default=0, blank=True)
    bodywear = models.IntegerField(default=0, blank=True)
    footwear = models.IntegerField(default=0, blank=True)
    # How do we handle inventory, errors, and message array's
    # inventory = ArrayField(models.CharField(max_length=255), default=list)
    errors = models.CharField(max_length=255, blank=True)
    messages = models.CharField(max_length=500, blank=True)

class Proof(models.Model):
    # May need to change
    proof = models.IntegerField(default=0, editable=False, blank=True)
    difficulty = models.IntegerField(default=0, blank=True)
    cooldown = models.IntegerField(default=100, editable=False, blank=True)
    errors = models.CharField(max_length=255, blank=True)
    messages = models.CharField(max_length=500, blank=True)
