from django.db import models


class Competition(models.Model):

    names_competition = (
        ('100m rasos', '100m rasos'),
        ('Lançamento de Dardo', 'Lançamento de Dardo')
    )
    competition = models.CharField(
        max_length=60,
        choices=names_competition
    )

    def __str__(self):
        return self.competition


class CreateCompetition(models.Model):

    name_athlete = models.CharField(max_length=255)
    weight_athlete = models.CharField(max_length=25)

    place_competition_op = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins')
    )

    age_athlete = models.CharField(max_length=25)
    height_athlete = models.CharField(max_length=25)
    name_competition = models.ForeignKey(
        Competition, on_delete=models.SET_NULL, null=True
    )
    place_competition = models.CharField(
        max_length=255,
        choices=place_competition_op
    )

    created_at = models.DateTimeField(auto_now_add=True)

    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_athlete


class DatabaseCompetition(models.Model):

    id_athlete = models.ForeignKey(
        CreateCompetition, on_delete=models.SET_NULL, null=True
    )
    name_competition = models.ForeignKey(
        Competition, on_delete=models.SET_NULL, null=True
    )
    meters = models.FloatField()
    time = models.FloatField()

    def __str__(self):
        return self.id_athlete
