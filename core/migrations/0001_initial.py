# Generated by Django 2.2.7 on 2019-11-23 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instagram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeUsuario', models.CharField(max_length=255, verbose_name='Nome de Usuário')),
                ('telefone', models.CharField(max_length=20, verbose_name='Telefone')),
            ],
            options={
                'ordering': ['nomeUsuario'],
                'verbose_name_plural': 'Instagram',
                'verbose_name': 'Instagram',
            },
        ),
    ]
