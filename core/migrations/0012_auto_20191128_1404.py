# Generated by Django 2.2.7 on 2019-11-28 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_sobrenosmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagemBanner', models.ImageField(upload_to='banner/', verbose_name='Banner')),
            ],
            options={
                'verbose_name': 'Banner',
            },
        ),
        migrations.AlterModelOptions(
            name='sobrenosmodel',
            options={'verbose_name': 'Sobre Nós'},
        ),
    ]