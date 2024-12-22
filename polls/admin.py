from django.contrib import admin

# Register your models here.
from .models import Question, Choice, Contributor, CandidateRestaurant


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date"]
    search_fields = ["question_text"]


class ContributorAdmin(admin.ModelAdmin):
    list_display = ['user', 'picture_url']
    search_fields = ['user__username']


class CandidateRestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'created_at', 'updated_at']
    search_fields = ['name']
    list_filter = ['created_at', 'updated_at']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(CandidateRestaurant, CandidateRestaurantAdmin)
