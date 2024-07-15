from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "email", "user_since", "birthday", "picture"]
    list_select_related = ['user']
    search_fields = ['user__first_name', 'user__last_name']
    list_editable = ["picture"]
    exclude = ["id", "created_at", "updated_at", "trashed_at"]

    def username(self, profile):
        return profile.user.username if profile.user else "null"
    def first_name(self, profile):
        return profile.user.first_name if profile.user else "null"
    def last_name(self, profile):
        return profile.user.last_name if profile.user else "null"
    def email(self, profile):
        return profile.user.email if profile.user else "null"
    def user_since(self, profile):
        return profile.user.date_joined.strftime('%B %d, %Y') if profile.user else "null"

    

@admin.register(models.Synch)
class SynchAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "creator_username", "picture"]
    list_select_related = ['creator']
    search_fields = ['name', 'creator_username']
    list_editable = ["name", "picture"]
    exclude = ["id", "created_at", "updated_at", "trashed_at"]
    def creator_username(self, synch):
        return synch.creator.user.username
    


@admin.register(models.SynchMembership)
class SynchMembershipAdmin(admin.ModelAdmin):
    list_display = ["id", "synch", "member"]
    list_select_related = ['member']
    list_editable = []
    exclude = ["id", "created_at", "updated_at", "trashed_at"]
  


@admin.register(models.Stream)
class StreamAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at", "synch", "name", "creator"]
    list_select_related = ['creator']
    list_editable = []
    exclude = ["id", "created_at", "updated_at", "trashed_at"]
  
