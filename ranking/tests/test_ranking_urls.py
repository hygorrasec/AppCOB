from django.test import TestCase
from django.urls import reverse


class CompetitionURLsTest(TestCase):
    def test_ranking_home_url_is_correct(self):
        ranking_url = reverse('ranking:home')
        self.assertEqual(ranking_url, '/ranking/')

    def test_ranking_modality_url_is_correct(self):
        modality_url = reverse('ranking:modality', kwargs={'id': 1})
        self.assertEqual(modality_url, '/ranking/1')
