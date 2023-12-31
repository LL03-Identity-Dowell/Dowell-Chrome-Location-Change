# Generated by Django 4.2.5 on 2023-09-18 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geo_search', '0006_language_remove_location_language_abbreviations_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='languages',
        ),
        migrations.AddField(
            model_name='location',
            name='languages',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='geo_search.language'),
        ),
    ]
