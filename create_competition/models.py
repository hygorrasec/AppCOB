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

    name_competition = models.ForeignKey(
        Competition, on_delete=models.SET_NULL, null=True
    )

    place_competition_op = (
        ('Acre', 'AC'),
        ('Alagoas', 'AL'),
        ('Amapá', 'AP'),
        ('Amazonas', 'AM'),
        ('Bahia', 'BA'),
        ('Ceará', 'CE'),
        ('Distrito Federal', 'DF'),
        ('Espírito Santo', 'ES'),
        ('Goiás', 'GO'),
        ('Maranhão', 'MA'),
        ('Mato Grosso', 'MT'),
        ('Mato Grosso do Sul', 'MS'),
        ('Minas Gerais', 'MG'),
        ('Pará', 'PA'),
        ('Paraíba', 'PB'),
        ('Paraná', 'PR'),
        ('Pernambuco', 'PE'),
        ('Piauí', 'PI'),
        ('Rio de Janeiro', 'RJ'),
        ('Rio Grande do Norte', 'RN'),
        ('Rio Grande do Sul', 'RS'),
        ('Rondônia', 'RO'),
        ('Roraima', 'RR'),
        ('Santa Catarina', 'SC'),
        ('São Paulo', 'SP'),
        ('Sergipe', 'SE'),
        ('Tocantins', 'TO')
    )

    place_competition = models.CharField(
        max_length=255,
        choices=place_competition_op
    )

    age_athlete = models.CharField(max_length=25)
    height_athlete = models.CharField(max_length=25)
    weight_athlete = models.CharField(max_length=25)
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
