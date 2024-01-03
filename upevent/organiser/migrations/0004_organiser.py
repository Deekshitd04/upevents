# Generated by Django 2.2.13 on 2022-07-28 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organiser', '0003_auto_20220728_1215'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organiser',
            fields=[
                ('org_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_join', models.DateField()),
                ('User_email', models.EmailField(max_length=70, unique=True)),
                ('mobile_no', models.CharField(max_length=50, unique=True)),
                ('address', models.TextField(default='', max_length=300)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
