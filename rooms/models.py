from django.db import models
from core.base import BaseModel
from django.utils.translation import gettext_lazy as _


class Room(BaseModel):
    name = models.CharField(max_length=250, blank=True, null=True, verbose_name = _('name'))
    image = models.ImageField(upload_to='room/', blank=True, null=True, verbose_name = _('image'))

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Room')
        verbose_name_plural = _('Room')


class RoomImage(BaseModel):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, null=True, verbose_name = _('room'))
    name = models.CharField(max_length=250, blank=True, verbose_name = _('name'))
    image = models.ImageField(upload_to='room_image/', blank=True, null=True, verbose_name = _('image'))

    def __str__(self):
        return f'{self.room.name}'

    class Meta:
        verbose_name = _('Room Image')
        verbose_name_plural = _('Room Image')
