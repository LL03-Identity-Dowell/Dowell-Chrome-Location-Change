# Generated by Django 4.2.5 on 2023-09-13 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo_search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Coordinates',
        ),
    ]
