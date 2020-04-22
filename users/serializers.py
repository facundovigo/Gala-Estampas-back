from rest_framework import serializers
from .models import *
from .models import Event


class EventSerializer():
    class Meta:
        model = Event
        fields = ('id', 'title', 'description')
