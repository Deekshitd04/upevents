# Generated by Django 2.2.13 on 2022-07-30 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organiser', '0013_package_package_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='category',
        ),
        migrations.AddField(
            model_name='package',
            name='category',
            field=models.CharField(choices=[('FOOD', 'FOOD'), ('DECORATION', 'DECORATION'), ('MUSIC', 'MUSIC'), ('LIGHTING', 'LIGHTING'), ('STAGE PROGRAM', 'STAGE PROGRAM')], default='MUSIC', max_length=30),
        ),
    ]
