# Generated by Django 2.2.13 on 2022-07-28 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organiser', '0002_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='desc',
            field=models.TextField(default='', max_length=5000),
        ),
    ]