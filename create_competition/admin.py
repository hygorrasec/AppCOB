from django.contrib import admin

from .models import Competition, CreateCompetition, DatabaseCompetition


@admin.register(DatabaseCompetition)
class DatabaseCompetitionAdmin(admin.ModelAdmin):
    pass


@admin.register(CreateCompetition)
class CreateCompetitionAdmin(admin.ModelAdmin):
    pass


@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    pass
