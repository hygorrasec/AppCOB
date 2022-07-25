from django.test import TestCase
from django.urls import reverse


class CompetitionURLsTest(TestCase):
    def test_home_home_url_is_correct(self):
        home_url = reverse('home:home')
        self.assertEqual(home_url, '/')
