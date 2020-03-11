# Generated by Django 2.2.5 on 2020-02-16 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0007_auto_20200216_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registry',
            name='artistName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='registry',
            name='musicbrainzArtistId',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='registry',
            name='musicbrainzTrackId',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='registry',
            name='trackName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='registry',
            name='userId',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
