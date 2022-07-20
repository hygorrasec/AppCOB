# from datetime import datetime, timedelta

from django.db import models

# def return_date_time():
#     now = datetime.now()
#     return now + timedelta(days=1)


class CreateCompetition(models.Model):

    name_competition_op = (
        ('100m rasos', '1'),
        ('Lançamento de Dardo', '2')
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

    name_competition = models.CharField(
        max_length=255,
        choices=name_competition_op
    )
    place_competition = models.CharField(
        max_length=255,
        choices=place_competition_op
    )

    # date_competition = models.DateTimeField(auto_now_add=True)

    created_at = models.DateTimeField(auto_now_add=True)

    name_athlete = models.CharField(max_length=255)
    age_athlete = models.CharField(max_length=25)
    height_athlete = models.CharField(max_length=25)
    weight_athlete = models.CharField(max_length=25)

    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_athlete
