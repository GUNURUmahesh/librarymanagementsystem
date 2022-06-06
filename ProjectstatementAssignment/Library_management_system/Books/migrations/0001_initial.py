# Generated by Django 3.2.13 on 2022-06-06 07:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(message='firstname must string and should not be less than 3 and greater than 12', regex='^(?=.{2,12}$)(?![_.])(?!.*[_.]{2})[a-zA-Z]+(?<![_.])$')])),
                ('Lastname', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(message='lastname must string and should not be less than 3 and greater than 12', regex='^(?=.{2,12}$)(?![_.])(?!.*[_.]{2})[a-zA-Z]+(?<![_.])$')])),
                ('Email', models.EmailField(max_length=50, unique=True)),
                ('Username', models.CharField(max_length=60, unique=True)),
                ('Password', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='password must contain 8 letters and a captail letter and a special character ', regex='^.*(?=.{8,})(?=.*\\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$')])),
                ('MobileNumber', models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 14 digits allowed.", regex='^\\+?1?\\d{9,14}$')])),
            ],
            options={
                'db_table': 'User_Data',
            },
        ),
    ]
