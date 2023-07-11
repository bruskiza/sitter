from django.contrib import admin
from .models import Seat, Building, Floor, Allocation

class SeatAdmin(admin.ModelAdmin):
    list_display = ["name", "floor", "what_three_word"]
    

class BuildingAdmin(admin.ModelAdmin):
    pass

class FloorAdmin(admin.ModelAdmin):
    pass

class AllocationAdmin(admin.ModelAdmin):
    list_display = ('owner', 'display_image')


admin.site.register(Seat, SeatAdmin)
admin.site.register(Building, BuildingAdmin)
admin.site.register(Floor, FloorAdmin)
admin.site.register(Allocation, AllocationAdmin)