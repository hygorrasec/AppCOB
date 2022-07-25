from django.test import TestCase
from django.urls import resolve, reverse
from register_result import views


class CompetitionViewsTest(TestCase):
    def test_register_result_home_views_function_is_correct(self):
        view = resolve(reverse('register_result:home'))
        self.assertIs(view.func, views.register_result)
