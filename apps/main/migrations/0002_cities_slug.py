# Generated by Django 5.1.1 on 2024-09-12 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cities',
            name='slug',
            field=models.SlugField(default=1, unique=True, verbose_name='URL'),
            preserve_default=False,
        ),
    ]
