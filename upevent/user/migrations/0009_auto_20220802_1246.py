# Generated by Django 2.2.13 on 2022-08-02 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20220802_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_image',
            field=models.URLField(null=True),
        ),
    ]
