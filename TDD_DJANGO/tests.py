from django.db import OperationalError
from django.db.models import Model
from django.test import TestCase
from django.urls import resolve

from TDD_DJANGO.models import User
from TDD_DJANGO.views import index


class TestModel(TestCase):
    def test_user_exists(self):
        self.assertIsInstance(User(), Model)


    def test_user_save(self):
        try:
            User().save()
        except OperationalError:
            self.fail("User().save() shouldn't raise Error")


    def test_user_name(self):
        U = User()
        U.prenom = 'Noé'
        U.save()
        self.assertEqual('Noé', User.objects.first().prenom)

    def test_user_nom(self):
        U = User()
        U.nom = 'Thiemard'
        U.save()
        self.assertEqual('Thiemard', User.objects.first().nom)

    def test_user_email(self):
        U = User()
        U.email = 'email@gmail.com'
        U.save()
        self.assertEqual('email@gmail.com', User.objects.first().email)

    def test_user_tel(self):
        U = User()
        U.tel = '766169366'
        U.save()
        self.assertEqual('766169366', User.objects.first().tel)



class URLTest(TestCase):
    def test_index_statut_200(self):
        reponse = self.client.get('/index/')
        self.assertEqual(200, reponse.status_code)

    def test_index_call_view(self):
        urlconfig = resolve('/index/')
        self.assertEqual(index, urlconfig.func)