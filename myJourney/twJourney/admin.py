from django.contrib import admin
from .models import LearningJourney, AboutMe

@admin.register(LearningJourney)
class LearningJourneyAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_started', 'date_completed')
    list_filter = ('date_started', 'date_completed')
    search_fields = ('title', 'description')

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_id', 'email')
    search_fields = ('name', 'student_id', 'email')