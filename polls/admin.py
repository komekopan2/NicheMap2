from django.contrib import admin

# Register your models here.
from .models import Question, Choice, Contributor, CandidateRestaurant


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date"]
    search_fields = ["question_text"]


@admin.register(Contributor)
class ContributorAdmin(admin.ModelAdmin):
    list_display = ['user', 'picture_url']
    search_fields = ['user__username']


@admin.register(CandidateRestaurant)
class CandidateRestaurantAdmin(admin.ModelAdmin):
    list_display = ['display_name', 'location', 'created_at', 'updated_at']
    search_fields = ['display_name']
    list_filter = ['created_at', 'updated_at']
