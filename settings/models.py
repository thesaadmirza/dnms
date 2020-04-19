from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, AbstractBaseUser
from django.urls import reverse
from django.db import models
from django.utils import timezone

ignore_field = set(["created_by", "updated_at", "updated_by", "created_at", "status"])
now = timezone.now()


class CommonInfo(models.Model):
    created_by = models.TextField()
    created_at = models.DateTimeField(default=now)
    updated_by = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(default=now)
    status = models.IntegerField(default=0)

    class Meta:
        abstract = True


def make_model_string(self):
    field_values = []
    for field in self._meta.get_fields():
        try:
            field_name = field.attname
            if field_name in ignore_field:
                continue
            field_values.append(str(self.__getattribute__(field.attname)))
        except:
            pass
    return '-'.join(field_values)


class Translation(models.Model):
    korean = models.CharField(primary_key=True, max_length=512)
    vietnamese = models.TextField(blank=True, null=True)
    english = models.TextField(blank=True, null=True)

    def __str__(self):
        return make_model_string(self)


class CompanyGroup(models.Model):
    company_group_name = models.CharField(primary_key=True, max_length=512)

    def __str__(self):
        return make_model_string(self)


class ItemGroup1(models.Model):
    item_group1_name = models.CharField(primary_key=True, max_length=512)
    item_group1_code = models.TextField()

    def __str__(self):
        return make_model_string(self)


class ItemGroup2(models.Model):
    item_group2_name = models.CharField(primary_key=True, max_length=512)
    item_group2_id = models.ForeignKey(ItemGroup1, on_delete=models.CASCADE)

    def __str__(self):
        return make_model_string(self)


class UnitGroup(models.Model):
    unit_group_name = models.CharField(primary_key=True, max_length=512)

    def __str__(self):
        return make_model_string(self)


class LanguageGroup(models.Model):
    language_group_name = models.CharField(primary_key=True, max_length=512)

    def __str__(self):
        return make_model_string(self)


class CountryGroup(models.Model):
    country_group_name = models.CharField(primary_key=True, max_length=512)

    def __str__(self):
        return make_model_string(self)


class Currency(models.Model):
    currency = models.CharField(primary_key=True, max_length=512)

    def __str__(self):
        return make_model_string(self)


class PlaceGroup(models.Model):
    place_group = models.CharField(primary_key=True, max_length=512)


class AccountGroup(models.Model):
    account_group = models.CharField(primary_key=True, max_length=512)
