# Generated by Django 5.0.3 on 2024-10-07 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_banners_options_alter_collections_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='collections',
            name='numimg',
            field=models.CharField(default='1', max_length=1, verbose_name='Слоган на русском'),
        ),
    ]
