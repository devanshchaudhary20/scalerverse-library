# Generated by Django 4.2.1 on 2023-06-27 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
