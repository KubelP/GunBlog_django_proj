from django.contrib import admin
from .models import Gun, Caliber, Comments

admin.site.register(Caliber)
admin.site.register(Gun)
admin.site.register(Comments)