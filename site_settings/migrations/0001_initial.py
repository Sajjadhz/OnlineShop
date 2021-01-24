# Generated by Django 3.1.5 on 2021-01-15 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان سایت')),
                ('address', models.CharField(max_length=400, verbose_name='آدرس')),
                ('phone', models.CharField(max_length=50, verbose_name='تلفن')),
                ('mobile', models.CharField(max_length=50, verbose_name='تلفن همراه')),
                ('fax', models.CharField(max_length=50, verbose_name='فکس')),
                ('email', models.EmailField(max_length=120, verbose_name='ایمیل')),
            ],
            options={
                'verbose_name': 'تنظیمات سایت',
                'verbose_name_plural': 'مدیریت تنظیمات',
            },
        ),
    ]
