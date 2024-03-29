# Generated by Django 2.2.6 on 2019-11-07 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rows', models.IntegerField()),
                ('columns', models.IntegerField()),
                ('max_allocation_matrix', models.CharField(max_length=128)),
                ('allocation_matrix', models.CharField(max_length=128)),
                ('available_vector', models.CharField(max_length=128)),
            ],
        ),
    ]
