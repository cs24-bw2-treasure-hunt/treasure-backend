from django.db import models
from django.contrib.postgres.fields import ArrayField

class Room(models.Model):
    room_id = models.IntegerField(primary_key=True, unique=True, editable=False)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    coordinates = models.CharField(max_length=32)
    players = models.CharField(max_length=255)
    items = models.CharField(max_length=255)
    exits = models.CharField(max_length=255)
    cooldown = models.IntegerField(default=100, editable=False)
    errors = models.CharField(max_length=255)
    messages = models.CharField(max_length=500)

    # May need adjustments for array fields. blank=True allows for empty fields. DOES NOT WORK WITH SQL
    # players = ArrayField(models.CharField(max_length=255), default=list)
    # items = ArrayField(models.CharField(max_length=255), default=list)
    # exits = ArrayField(models.CharField(max_length=255), default=list)
    # cooldown = models.IntegerField(editable=False)
    # errors = ArrayField(models.CharField(max_length=255), default=list)
    # messages = ArrayField(models.CharField(max_length=255), default=list)

class Inventory(models.Model):
    name = models.CharField(max_length=20)
    cooldown = models.IntegerField(default=100)
    encumbrance = models.IntegerField(default=0)
    strength = models.IntegerField(default=10)
    speed = models.IntegerField(default=10)
    gold = models.IntegerField(default=0)
    bodywear = models.IntegerField(default=0)
    footwear = models.IntegerField(default=0)
    # How do we handle inventory, errors, and message array's
    # inventory = ArrayField(models.CharField(max_length=255), default=list)
    errors = models.CharField(max_length=255)
    messages = models.CharField(max_length=500)

class Proof(models.Model):
    # May need to change
    proof = models.IntegerField(default=0, editable=False)
    difficulty = models.IntegerField(default=0)
    cooldown = models.IntegerField(default=100, editable=False)
    errors = models.CharField(max_length=255)
    messages = models.CharField(max_length=500)
