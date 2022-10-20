from django.db import models

class Relative (models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    birthday = models.DateField()
    relation_ship = models.CharField(max_length=40)

    def __str__(self):
        return f"Hola mi nombre es {self.name}, tengo {self.age} años y soy {self.relation_ship} de Fabri."

