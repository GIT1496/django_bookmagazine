# Generated by Django 4.1.3 on 2022-12-07 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Boormag', '0009_alter_author_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='date_of_death2',
            field=models.CharField(choices=[('По сей день', 'По сей день')], max_length=120, verbose_name='Дата смерти автора'),
        ),
    ]
