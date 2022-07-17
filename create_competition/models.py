from django.db import models


class CreateCompetition(models.Model):

    name_competition = models.CharField(max_length=255)
    place_competition = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    name_athlete = models.CharField(max_length=255)
    age_athlete = models.CharField(max_length=25)
    height_athlete = models.CharField(max_length=25)
    weight_athlete = models.CharField(max_length=25)

    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_competition
