from django.test import TestCase

# Create your tests here.
from blog.models import Wpis


class TestBlogRoutes(TestCase):
    def test_main_page_of_blog_exists(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

class TestWpisModel(TestCase):
    def test_can_create_wpis(self):
        w = Wpis(
            tytul = "Ala ma kota",
            tresc = "Ala ma kota 2"
        )
        w.save()

        self.assertEqual(w, Wpis.objects.last())
        w.delete()