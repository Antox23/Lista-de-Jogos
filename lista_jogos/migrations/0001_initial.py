# Generated by Django 4.0.3 on 2022-03-16 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('categoria', models.CharField(max_length=50)),
                ('modo_de_jogo', models.CharField(max_length=50)),
                ('plataformas', models.CharField(max_length=50)),
                ('sinopse', models.TextField()),
                ('data_lancamento', models.DateField()),
            ],
        ),
    ]
