from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField('Nome:', max_length=100)
    last_name = models.CharField('Sobrenome', max_length=100)
    car_id = models.IntegerField('Id Carro:')
    customer_need = models.CharField('Necessidade do cliente:', max_length=100)
    car_title = models.CharField('Nome do carro:', max_length=100)
    city = models.CharField('Cidade:', max_length=100)
    state = models.CharField('Estado:',max_length=100)
    email = models.CharField('Email:',max_length=100)
    phone = models.CharField('Telefone:',max_length=100)
    message = models.TextField('Mensagem:',blank=True, max_length=100)
    user_id = models.IntegerField('Id Usuário:',blank=True)
    create_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self) -> str:
        return self.email