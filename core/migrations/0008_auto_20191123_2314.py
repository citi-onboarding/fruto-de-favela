# Generated by Django 2.2.7 on 2019-11-24 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20191124_0013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='imagem',
        ),
        migrations.RemoveField(
            model_name='formulario',
            name='imagem',
        ),
    ]
