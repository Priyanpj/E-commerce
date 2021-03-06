# Generated by Django 2.2 on 2021-12-03 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='picture')),
                ('price', models.IntegerField()),
                ('offer', models.BooleanField(default=False)),
                ('prod_cat', models.CharField(max_length=100)),
            ],
        ),
    ]
