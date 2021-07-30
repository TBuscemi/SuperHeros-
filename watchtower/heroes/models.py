from django.db import models

# Create your models here.

class Heroes(models.Model):
    super_hero_name = models.CharField(max_length=50)
    alter_ego = models.CharField(max_length=50)
    primary_superHero_ability = models.CharField(max_length=50)
    secondary_superHero_ability = models.CharField(max_length=50)
    catchphrase = models.CharField(max_length=50)

    def __str__(self):
        return self.super_hero_name       
