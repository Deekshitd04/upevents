# Generated by Django 2.2.13 on 2022-08-01 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20220731_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('u_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=30, unique=True)),
                ('user_mbl_no', models.CharField(max_length=60, unique=True)),
                ('user_dob', models.DateField()),
                ('user_gender', models.CharField(max_length=30)),
                ('user_image', models.ImageField(default='', upload_to='UserProfile/images')),
            ],
        ),
    ]
