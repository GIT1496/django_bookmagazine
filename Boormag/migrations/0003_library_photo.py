# Generated by Django 4.1.3 on 2022-11-04 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Boormag', '0002_library_cover_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='photo',
            field=models.ImageField(null=True, upload_to='image/%Y/%m/%d', verbose_name='Фотография'),
        ),
    ]