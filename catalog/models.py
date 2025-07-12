from django.db import models
from core.base import BaseModel
from rooms.models import Room
from django.utils.translation import gettext_lazy as _


COLLECTION_TYPE = (
    (1, '---'),
    (2, 'New'),
    (3, 'Sale'),
    (4, 'Hit'),
)


class Catalog(BaseModel):
    name = models.CharField(max_length=250, blank=True, null=True, verbose_name = _('name'))
    image = models.ImageField(upload_to='catalog_img/', blank=True, verbose_name = _('image'))

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Catalog')
        verbose_name_plural = _('Catalog')


class Style(BaseModel):
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name='styles', verbose_name = _('catalog'))
    name = models.CharField(max_length=250, blank=True, null=True, verbose_name = _('name'))

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Style')
        verbose_name_plural = _('Style')


class Color(BaseModel):
    name = models.CharField(max_length=250, blank=True, null=True, verbose_name = _('name'))

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Color')
        verbose_name_plural = _('Color')


class Price(BaseModel):
    from_price = models.IntegerField(default=0, verbose_name = _('from_price'))
    to_price = models.IntegerField(default=0, verbose_name = _('to_price'))

    def __str__(self):
        return f'{self.from_price} {self.to_price}'

    class Meta:
        verbose_name = _('Price')
        verbose_name_plural = _('Price')


class Carpet(BaseModel):
    name = models.CharField(max_length=250, blank=True, null=True, verbose_name = _('name'))
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, verbose_name = _('catalog'))
    image = models.ImageField(upload_to='carpet/', blank=True, verbose_name = _('image'))
    collection_type = models.IntegerField(choices=COLLECTION_TYPE, default=0, verbose_name = _('collection_type'))

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Carpet')
        verbose_name_plural = _('Carpet')


class CarpetModel(BaseModel):
    model = models.ForeignKey(Carpet, on_delete=models.CASCADE, verbose_name = _('model'))
    style = models.ForeignKey(Style, on_delete=models.CASCADE, verbose_name = _('style'))
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name = _('room'))
    name = models.CharField(max_length=250, blank=True, null=True, verbose_name = _('name'))
    price = models.FloatField(default=0, verbose_name = _('price'))
    discount = models.FloatField(default=0, verbose_name = _('discount'))
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, verbose_name = _('catalog'))
    color = models.ForeignKey(Color, on_delete=models.CASCADE, verbose_name = _('color'))
    image = models.ImageField(upload_to='carpet_model/', blank=True, verbose_name = _('image'))
    collection_type = models.IntegerField(choices=COLLECTION_TYPE, default=0, verbose_name = _('collection_type'))

    def __str__(self):
        return f'{self.name} || {self.color.name}'

    class Meta:
        verbose_name = _('Carpet Model')
        verbose_name_plural = _('Carpet Model')


class Character(BaseModel):
    name = models.CharField(max_length=300, verbose_name = _('name'))

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Character')
        verbose_name_plural = _('Character')


class CharacterDetail(BaseModel):
    title = models.CharField(max_length=250, blank=True)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, blank=True, verbose_name = _('character'))
    model = models.ForeignKey(CarpetModel, on_delete=models.CASCADE, blank=True, verbose_name = _('model'))
    detail = models.CharField(max_length=250, verbose_name = _('detail'))

    def __str__(self):
        return f'{self.detail}'

    class Meta:
        verbose_name = _('Character Detail')
        verbose_name_plural = _('Character Detail')


class CarpetModelImages(BaseModel):
    carpet_model = models.ForeignKey(CarpetModel, on_delete=models.CASCADE, verbose_name = _('carpet_model'))
    image = models.ImageField(upload_to='carpet_model_images/', blank=True, null=True, verbose_name = _('image'))

    def __str__(self):
        return f'{self.carpet_model.name}'

    class Meta:
        verbose_name = _('Carpet Model Images')
        verbose_name_plural = _('Carpet Model Images')


class Shape(BaseModel):
    name = models.CharField(max_length=250, blank=True, null=True, verbose_name = _('name'))

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Shape')
        verbose_name_plural = _('Shape')


class Size(BaseModel):
    carpet_model = models.ForeignKey(CarpetModel, on_delete=models.CASCADE, verbose_name = _('carpet_model'))
    shape = models.ForeignKey(Shape, on_delete=models.CASCADE, verbose_name = _('shape'))
    width = models.IntegerField(default=0, verbose_name = _('width'))
    length = models.IntegerField(default=0, verbose_name = _('length'))
    price = models.FloatField(default=0, verbose_name = _('price'))
    discount = models.FloatField(default=0, verbose_name = _('discount'))

    def __str__(self):
        return f'{self.width} x {self.length}'

    class Meta:
        verbose_name = _('Size')
        verbose_name_plural = _('Size')




