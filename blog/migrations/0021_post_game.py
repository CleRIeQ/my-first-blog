# Generated by Django 3.2.9 on 2021-11-09 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20211106_0618'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='game',
            field=models.PositiveSmallIntegerField(choices=[(1, 'WOT'), (1, 'Pubg')], default=1),
        ),
    ]