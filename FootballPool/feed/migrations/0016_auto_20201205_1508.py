# Generated by Django 3.0.9 on 2020-12-05 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0015_auto_20201130_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dislike',
            name='value',
            field=models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='DisLike', max_length=10),
        ),
    ]
