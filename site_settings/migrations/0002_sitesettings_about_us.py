# Generated by Django 3.1.5 on 2021-01-15 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='about_us',
            field=models.TextField(blank=True, null=True, verbose_name='درباره ما'),
        ),
    ]
