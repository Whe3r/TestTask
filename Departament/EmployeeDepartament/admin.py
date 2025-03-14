from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Department, Employee


@admin.register(Department)
class DepartmentAdmin(MPTTModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ('name',)
    mptt_level_indent = 30


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'department')
    list_filter = ('department', 'position')
    search_fields = ('name', 'position')
    autocomplete_fields = ['department']
