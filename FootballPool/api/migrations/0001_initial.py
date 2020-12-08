# Generated by Django 3.0.9 on 2020-12-08 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=255)),
                ('away_score', models.IntegerField()),
                ('home_score', models.IntegerField()),
                ('current_perriod', models.IntegerField()),
                ('time_remaining', models.CharField(max_length=255)),
            ],
        ),
    ]
