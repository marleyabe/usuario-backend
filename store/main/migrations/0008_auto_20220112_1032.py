# Generated by Django 3.1.7 on 2022-01-12 13:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20220111_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default=0, max_length=25, verbose_name='Name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='review',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Review'),
        ),
    ]
