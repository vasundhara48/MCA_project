from django.contrib import admin
from .models import UserProfile, UserSkill, Analysis

admin.site.register(UserProfile)
admin.site.register(UserSkill)
admin.site.register(Analysis)
