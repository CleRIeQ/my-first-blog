# Generated by Django 3.2.7 on 2021-10-22 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_texthalf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='texthalf',
        ),
    ]
