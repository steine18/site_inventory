from django.contrib import admin
from .models import Equipment_type, Equipment_model, Equipment, Site, Site_equipment, Deployment, Shop_log, Equipment_test
# Register your models here.
admin.site.register(Site)
admin.site.register(Equipment_type)
admin.site.register(Equipment_model)
admin.site.register(Equipment)
admin.site.register(Site_equipment)
admin.site.register(Deployment)
admin.site.register(Shop_log)
admin.site.register(Equipment_test)