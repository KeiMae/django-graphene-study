from django.contrib import admin
from .models import Companies, Seekers, Side
# Register your models here.

@admin.register(Companies)
class CompanyAdmin(admin.ModelAdmin):
    model = Companies
    fields = ["name", "address"]

@admin.register(Seekers)
class SeekerAdmin(admin.ModelAdmin):
    model = Seekers
    fields = ["seeker", "side"]


@admin.register(Side)
class SiteAdmin(admin.ModelAdmin):
    model = Side
    fields = ["name",]