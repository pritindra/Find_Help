from django.contrib import admin
from .models import AcceptedAssist, AcceptedOffer

# Register your models here.
admin.site.register(AcceptedOffer)
admin.site.register(AcceptedAssist)