# Generated by Django 4.2.1 on 2023-06-27 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=100)),
                ('book_description', models.CharField(max_length=100)),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookStatus',
            fields=[
                ('status_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('user_uid', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manage_library.book')),
            ],
        ),
    ]
