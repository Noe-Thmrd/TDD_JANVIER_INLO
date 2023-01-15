from django.db.models import Model, TextField


class User(Model):
    prenom = TextField()
    nom = TextField()
    email = TextField()
    tel = TextField()