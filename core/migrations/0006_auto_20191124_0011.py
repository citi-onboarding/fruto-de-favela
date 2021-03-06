# Generated by Django 2.2.7 on 2019-11-24 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_banner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'ordering': ['title'], 'verbose_name': 'Imagem Banner', 'verbose_name_plural': 'Imagens Banner'},
        ),
        migrations.AddField(
            model_name='banner',
            name='title',
            field=models.CharField(default=12, max_length=100, verbose_name='Título'),
            preserve_default=False,
        ),
    ]
