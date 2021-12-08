# Generated by Django 3.2.3 on 2021-12-08 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20211106_0618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='N/G', max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='textinfo',
            field=models.CharField(default='О чем ваш текст?', max_length=250),
        ),
    ]