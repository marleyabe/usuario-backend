# Generated by Django 4.0.1 on 2022-01-14 18:13

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_rename_avatar_usuario_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='file',
            field=models.FileField(default='', upload_to=main.models.filepath),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
