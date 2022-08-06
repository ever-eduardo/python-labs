from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class HomePageTest(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):
        respose = self.client.get(reverse("home"))
        self.assertEqual(respose.status_code, 200)


class AboutPageTest(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        respose = self.client.get(reverse("about"))
        self.assertEqual(respose.status_code, 200)