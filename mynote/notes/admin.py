from django.contrib import admin
from .models import Notes
from django.contrib.auth.models import User
from notes.models import UserAccount
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(Notes)
class NotesModelAdmin(admin.ModelAdmin):
    list_display=('id','note','time_created','time_updated','image')
# admin.site.register(Notes,NotesModelAdmin)
# admin.site.unregister(User)
@admin.register(UserAccount)
class UserAccountModelAdmin(admin.ModelAdmin):
    list_display=('id','user','image')


    