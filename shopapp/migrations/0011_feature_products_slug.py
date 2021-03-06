# Generated by Django 2.2 on 2021-12-07 12:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0010_auto_20211207_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature_products',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=250, unique=True),
            preserve_default=False,
        ),
    ]
