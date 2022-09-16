from django.contrib import admin
from .models import Member
# Register your models here.

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('member_name', 'member_position')
    search_fields = ('member_name', 'member_position')