# Generated by Django 3.0.3 on 2020-02-05 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.IntegerField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('coordinates', models.CharField(max_length=32)),
                ('players', models.CharField(max_length=255)),
                ('items', models.CharField(max_length=255)),
                ('exits', models.CharField(max_length=255)),
                ('cooldown', models.IntegerField(default=100, editable=False)),
                ('errors', models.CharField(max_length=255)),
                ('messages', models.CharField(max_length=500)),
            ],
        ),
    ]