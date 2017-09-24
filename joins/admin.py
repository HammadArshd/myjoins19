from django.contrib import admin

# Register your models here.
from .models import Join

class JoinAdmin(admin.ModelAdmin):
    # list_display = ["email", "timestamp", "__str__", "updated"]
    list_display = ["email", "timestamp", "ip_address", "updated"]
    class Meta:
        model = Join

admin.site.register(Join, JoinAdmin)
