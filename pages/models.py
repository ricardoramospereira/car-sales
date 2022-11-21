from django.db import models

# Create your models here.
class Team(models.Model):
    first_name = models.CharField('Nome', max_length=100)
    last_name = models.CharField('Sobrenome', max_length=100)
    designation = models.CharField('Função', max_length=100)
    photo = models.ImageField('Foto', upload_to='photos/%Y/%m/%d/')
    facebook_link = models.URLField('Facebook', max_length=100)
    twitter_link = models.URLField('Twitter', max_length=100)
    google_plus_link = models.URLField('Google', max_length=100)
    created_date = models.DateTimeField('Data de Criação', auto_now_add=True)

    def __str__(self) -> str:
        return self.first_name