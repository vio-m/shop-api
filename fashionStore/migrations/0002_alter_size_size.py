# Generated by Django 4.0.5 on 2023-02-03 09:54

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('fashionStore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='size',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('36', '36'), ('37', '37'), ('38', '38'), ('39', '39')], max_length=11),
        ),
    ]
