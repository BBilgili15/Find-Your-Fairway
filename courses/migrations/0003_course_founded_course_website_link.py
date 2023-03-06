# Generated by Django 4.1.7 on 2023-02-28 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='founded',
            field=models.IntegerField(default=1900),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='website_link',
            field=models.CharField(default='1900', max_length=255),
            preserve_default=False,
        ),
    ]