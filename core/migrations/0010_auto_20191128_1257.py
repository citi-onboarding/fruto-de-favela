# Generated by Django 2.2.7 on 2019-11-28 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20191124_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='NossosProgramasModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Título')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('imagem', models.ImageField(upload_to='nossosProgramas/', verbose_name='Imagem')),
            ],
            options={
                'ordering': ['titulo'],
                'verbose_name': 'Nossos Programas',
                'verbose_name_plural': 'Nossos Programas',
            },
        ),
        migrations.DeleteModel(
            name='Banner',
        ),
        migrations.DeleteModel(
            name='Formulario',
        ),
        migrations.DeleteModel(
            name='Instagram',
        ),
    ]
