# Generated by Django 3.0.9 on 2020-12-16 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='game_id',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
