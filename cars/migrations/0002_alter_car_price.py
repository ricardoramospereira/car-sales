# Generated by Django 4.1.3 on 2022-11-22 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="price",
            field=models.IntegerField(verbose_name="Preço"),
        ),
    ]
