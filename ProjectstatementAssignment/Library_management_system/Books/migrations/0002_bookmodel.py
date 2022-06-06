# Generated by Django 3.2.13 on 2022-06-06 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AuthorName', models.CharField(max_length=250)),
                ('BookName', models.CharField(max_length=250)),
                ('BookPublishedOn', models.CharField(max_length=250)),
                ('BookId', models.CharField(max_length=250)),
                ('Status', models.CharField(choices=[('Borrowed', 'Borrowed'), ('Avaliable', 'Avaliable')], max_length=10)),
                ('AdminId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LibraryId', to='Books.adminmodel')),
            ],
            options={
                'db_table': 'Book_Table',
            },
        ),
    ]
