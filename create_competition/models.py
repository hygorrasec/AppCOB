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
        ('Acre', 'Acre'),
        ('Alagoas', 'Alagoas'),
        ('Amapá', 'Amapá'),
        ('Amazonas', 'Amazonas'),
        ('Bahia', 'Bahia'),
        ('Ceará', 'Ceará'),
        ('Distrito Federal', 'Distrito Federal'),
        ('Espírito Santo', 'Espírito Santo'),
        ('Goiás', 'Goiás'),
        ('Maranhão', 'Maranhão'),
        ('Mato Grosso', 'Mato Grosso'),
        ('Mato Grosso do Sul', 'Mato Grosso do Sul'),
        ('Minas Gerais', 'Minas Gerais'),
        ('Pará', 'Pará'),
        ('Paraíba', 'Paraíba'),
        ('Paraná', 'Paraná'),
        ('Pernambuco', 'Pernambuco'),
        ('Piauí', 'Piauí'),
        ('Rio de Janeiro', 'Rio de Janeiro'),
        ('Rio Grande do Norte', 'Rio Grande do Norte'),
        ('Rio Grande do Sul', 'Rio Grande do Sul'),
        ('Rondônia', 'Rondônia'),
        ('Roraima', 'Roraima'),
        ('Santa Catarina', 'Santa Catarina'),
        ('São Paulo', 'São Paulo'),
        ('Sergipe', 'Sergipe'),
        ('Tocantins', 'Tocantins')
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
