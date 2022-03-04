from django.contrib import admin
from .models import NewUser
from django.contrib import messages


# Register your models here.

@admin.register(NewUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'first_name', 'last_name',
                    'role', 'is_staff', 'active')
    list_filter = ('role', 'start_date')
    search_fields = ['user_name', 'email']

    def active(self, obj):
        return obj.is_active == 1

    active.boolean = True

    def make_active(modeladmin, request, queryset):
        queryset.update(is_active=1)
        messages.success(
            request, "Selected Record(s) Marked as Active Successfully !!")

    def make_inactive(modeladmin, request, queryset):
        queryset.update(is_active=0)
        messages.success(
            request, "Selected Record(s) Marked as Inactive Successfully !!")

    admin.site.add_action(make_active, "Make Active")
    admin.site.add_action(make_inactive, "Make Inactive")

    def has_delete_permission(self, request, obj=None):
        return False
