# Generated by Django 4.2.2 on 2023-06-12 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50)),
                ('mob_num', models.IntegerField(max_length=10)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]