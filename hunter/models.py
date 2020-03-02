from django.db import models

"""
Working with:
    {
    "room_id": 0,
    "title": "Room 0",
    "description": "You are standing in an empty room.",
    "coordinates": "(60,60)",
    "players": [],
    "items": ["small treasure"],
    "exits": ["n", "s", "e", "w"],
    "cooldown": 60.0,
    "errors": [],
    "messages": []
    }
"""

class Rooms(models.Model):
    room_id = models.IntegerField(primary_key=True, unique=True, editable=False)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    coordinates = models.CharField(max_length=256)
    players = models.CharField(max_length=512, blank=True)
    items = models.CharField(max_length=256, blank=True)
    exits = models.CharField(max_length=64)
    cooldown = models.IntegerField(max_length=64)
    errors = models.CharField(max_length=256, blank=True)
    messages = models.CharField(max_length=512, blank=True)