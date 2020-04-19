from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _


from .models import *


# Register your models here.
admin.site.register(Translation)
admin.site.register(CompanyGroup)
admin.site.register(ItemGroup1)
admin.site.register(ItemGroup2)
admin.site.register(UnitGroup)
admin.site.register(LanguageGroup)
admin.site.register(CountryGroup)
admin.site.register(Currency)
admin.site.register(PlaceGroup)
admin.site.register(AccountGroup)
