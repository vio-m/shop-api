# Generated by Django 4.0.5 on 2023-02-13 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashionStore', '0004_subscription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='trending',
        ),
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]