# Generated by Django 2.2.7 on 2019-11-28 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_parceirosmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerContatoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagam', models.CharField(blank=True, max_length=100, null=True, verbose_name='Instagram')),
                ('telefone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefone')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail')),
            ],
            options={
                'verbose_name': 'Contatos',
            },
        ),
    ]
