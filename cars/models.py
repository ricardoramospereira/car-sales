from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

####################test
# from multiselectfield import MultiSelectField

# Create your models here.
class Car(models.Model):

    state_choice = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
        ('DF', 'Distrito Federal'),
    )

    year_choice = []
    for c in range(2000, (datetime.now().year+1)):
        year_choice.append((c,c))

    features_choices = (
        ('Controle de Cruzeiro', 'Controle de Cruzeiro'),
        ('Interface de áudio', 'Interface de áudio'),
        ('Airbags', 'Airbags'),
        ('Ar Condicionado', 'Ar Condicionado'),
        ('Aquecimento do Assento', 'Aquecimento do Assento'),
        ('Sistema de Alarme', 'Sistema de Alarme'),
        ('Assistente de estacionamento', 'Assistente de estacionamento'),
        ('Direção Hidráulica', 'Direção Hidráulica'),
        ('Câmera de Ré', 'Câmera de Ré'),
        ('Injeção Direta de Combustível', 'Injeção Direta de Combustível'),
        ('Partida/Parada Automática', 'Partida/Parada Automática'),
        ('Defletor de vento', 'Defletor de vento'),
        ('Fone Bluetooth', 'Fone Bluetooth'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    car_title = models.CharField('Carro', max_length=255)
    state = models.CharField('Estado', choices=state_choice, max_length=100)
    city = models.CharField('Cidade', max_length=100)
    color = models.CharField('Cor', max_length=100)
    model = models.CharField('Modelo', max_length=100)
    year = models.IntegerField(('Ano'), choices=year_choice)
    condition = models.CharField('Condição', max_length=100)
    price = models.IntegerField('Preço')
    description = RichTextField('Descrição')
    car_photo = models.ImageField('foto', upload_to='photos/%d/%m/%Y')
    car_photo_1 = models.ImageField('foto', upload_to='photos/%d/%m/%Y', blank=True)
    car_photo_2 = models.ImageField('foto', upload_to='photos/%d/%m/%Y', blank=True)
    car_photo_3 = models.ImageField('foto', upload_to='photos/%d/%m/%Y', blank=True)
    car_photo_4 = models.ImageField('foto', upload_to='photos/%d/%m/%Y', blank=True)
    features = models.CharField('Recursos', choices=features_choices, max_length=100)
    body_style = models.CharField('Estilo', max_length=100)
    engine = models.CharField('Motor', max_length=100)
    transmition = models.CharField('Transmissão', max_length=100)
    interior = models.CharField('Interior', max_length=100)
    miles = models.IntegerField('KM')
    doors = models.CharField('Portas', choices=door_choices, max_length=100)
    passengers = models.IntegerField('Passageiros')
    vin_no = models.CharField(max_length=100)
    milage = models.IntegerField('KMs')
    fuel_type = models.CharField('Tipo de combustível', max_length=50)
    no_of_owners = models.CharField('Nº Proprietários', max_length=100)
    is_featured = models.BooleanField('Destaques', default=False)
    created_date = models.DateField('Data de Criação', default=datetime.now, blank=True)

    def __str__(self) -> str:
        return self.car_title