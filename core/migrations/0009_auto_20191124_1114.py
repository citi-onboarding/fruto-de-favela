# Generated by Django 2.2.7 on 2019-11-24 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20191123_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='imagem',
            field=models.ImageField(default=1, upload_to='banner/', verbose_name='Imagem'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formulario',
            name='imagem',
            field=models.ImageField(default=1, upload_to='formulario/', verbose_name='Imagem'),
            preserve_default=False,
        ),
    ]
