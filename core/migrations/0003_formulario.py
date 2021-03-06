# Generated by Django 2.2.7 on 2019-11-23 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191123_2300'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Título')),
                ('texto', models.TextField(blank=True, null=True, verbose_name='Texto')),
                ('url', models.URLField(max_length=1000, verbose_name='Link')),
                ('imagem', models.ImageField(upload_to='formulario/', verbose_name='Imagem')),
            ],
            options={
                'ordering': ['titulo'],
                'verbose_name': 'Formulário',
                'verbose_name_plural': 'Formulários',
            },
        ),
    ]
