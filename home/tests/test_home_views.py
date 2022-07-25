from django.test import TestCase
from django.urls import resolve, reverse
from home import views


class HomeViewsTest(TestCase):
    def test_home_views_function_is_correct(self):
        view = resolve(reverse('home:home'))
        self.assertIs(view.func, views.home)
