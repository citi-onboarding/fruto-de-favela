# Generated by Django 2.2.7 on 2019-11-24 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20191124_0011'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'ordering': ['titulo'], 'verbose_name': 'Imagem Banner', 'verbose_name_plural': 'Imagens Banner'},
        ),
        migrations.RenameField(
            model_name='banner',
            old_name='title',
            new_name='titulo',
        ),
    ]
