from django.test import TestCase
from django.urls import reverse


class CompetitionURLsTest(TestCase):
    def test_register_result_home_url_is_correct(self):
        register_result_url = reverse('register_result:home')
        self.assertEqual(register_result_url, '/register_result/')
