from django.db import models
from settings.models import *


class Place(CommonInfo):
    place_name = models.TextField()
    place_group = models.ForeignKey(PlaceGroup, on_delete=models.DO_NOTHING)
    place_country = models.ForeignKey(CountryGroup, on_delete=models.DO_NOTHING)


class Item(CommonInfo):
    item_code = models.CharField(unique=True, max_length=512)
    maker = models.TextField(blank=True, null=True)
    item_group1 = models.ForeignKey(ItemGroup1, on_delete=models.DO_NOTHING)
    item_group2 = models.ForeignKey(ItemGroup2, on_delete=models.DO_NOTHING)
    item_name = models.TextField()
    item_spec = models.TextField()
    unit = models.ForeignKey(UnitGroup, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='%Y/%m/%d', blank=True)
