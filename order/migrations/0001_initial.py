# Generated by Django 3.1.5 on 2021-01-15 21:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0006_auto_20210114_2345'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_paid', models.BooleanField(verbose_name='پرداخت شده')),
                ('payment_date', models.DateTimeField(blank=True, null=True, verbose_name='تاریخ پرداخت')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='خریدار')),
            ],
            options={
                'verbose_name': 'سبد خرید',
                'verbose_name_plural': 'سبد های خرید کاربران',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(verbose_name='قیمت محصول')),
                ('count', models.IntegerField(verbose_name='تعداد')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order', verbose_name='سبد خرید')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'جزئیات محصول',
                'verbose_name_plural': 'اطلاعات جزئیات محصول',
            },
        ),
    ]
