from django.test import TestCase

from .models import News

from django.db.models.fields.files import ImageFieldFile, FieldFile


# class TrainingModelTestCase(TestCase):
#     def setUp(self):
#         self.training = News.objects.create(
#             name="SuperName",
#             category="MegaCategory",
#             full_text="UltraText",
#             date="2022-01-22",
#             slug="Puper-slug"
#         )
#
#     def test_training_title(self):
#         self.assertEqual(str(self.training.name), 'SuperName')
#
#     def test_training_date(self):
#         self.assertEqual(str(self.training.date), '2022-01-22')
#
#     def test_training_category(self):
#         self.assertEqual(str(self.training.category), 'MegaCategory')
#
#     def test_training_slug(self):
#         self.assertEqual(str(self.training.slug), 'Puper-slug')
#
#     def test_training_full_text(self):
#         self.assertEqual(str(self.training.full_text), 'UltraText')
#

class TrainingViewsTestCase(TestCase):
    def test_main_page_status_code(self):
        response = self.client.get('main')
        self.assertEqual(response.status_code, 200)

    def test_addnews_page_status_code(self):
        response = self.client.get('addnews')
        self.assertEqual(response.status_code, 200)

    def test_accounts_profile_page_status_code(self):
        response = self.client.get('news')
        self.assertEqual(response.status_code, 200)

    def test_img_page_status_code(self):
        response = self.client.get('img')
        self.assertEqual(response.status_code, 200)

    def test_cookie_page_status_code(self):
        response = self.client.get('cookie')
        self.assertEqual(response.status_code, 200)

    def test_delcookie_page_status_code(self):
        response = self.client.get('delcookie')
        self.assertEqual(response.status_code, 200)

    def test_registr_page_status_code(self):
        response = self.client.get('registr')
        self.assertEqual(response.status_code, 200)

    def test_logout_page_status_code(self):
        response = self.client.get('logout')
        self.assertEqual(response.status_code, 200)

    def test_slug_page_status_code(self):
        response = self.client.get('slug')
        self.assertEqual(response.status_code, 200)
