# Generated by Django 2.2.7 on 2019-11-28 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20191128_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='SobreNosModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quemSomos', models.TextField(verbose_name='Quem Somos?')),
                ('acolher', models.TextField(verbose_name='Acolher')),
                ('desenvolver', models.TextField(verbose_name='Desenvolver')),
                ('encaminhar', models.TextField(verbose_name='Encaminhar')),
            ],
            options={
                'verbose_name': 'Sobre Nós',
                'verbose_name_plural': 'Sobre Nós',
            },
        ),
    ]
