# Generated by Django 3.1.5 on 2021-01-13 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_auto_20210114_0011'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'برچسب', 'verbose_name_plural': 'برچسب ها'},
        ),
    ]