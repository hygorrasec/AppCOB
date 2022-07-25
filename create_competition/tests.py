from django.test import TestCase
from django.urls import reverse


class CompetitionURLsTest(TestCase):
    def test_create_competition_home_url_is_correct(self):
        create_competition_url = reverse('create_competition:home')
        self.assertEqual(create_competition_url, '/create_competition/')
