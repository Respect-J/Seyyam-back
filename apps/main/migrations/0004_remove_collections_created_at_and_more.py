# Generated by Django 5.0.3 on 2024-10-07 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_collections_numimg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collections',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='collections',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='collections',
            name='title_ru',
        ),
        migrations.RemoveField(
            model_name='collections',
            name='title_uz',
        ),
        migrations.RemoveField(
            model_name='collections',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='collections',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='collections',
            name='numimg',
            field=models.CharField(default='1', max_length=1, verbose_name='номер фото'),
        ),
    ]
