from django.contrib import admin
from first_up.models import topic, Webpage, AccessRecord

# Register your models here.
admin.site.register(topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)