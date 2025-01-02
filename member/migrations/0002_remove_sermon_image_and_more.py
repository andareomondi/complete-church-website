# Generated by Django 5.1.1 on 2025-01-02 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sermon',
            name='image',
        ),
        migrations.RemoveField(
            model_name='sermon',
            name='preacher_profile_pic',
        ),
        migrations.AddField(
            model_name='churchimage',
            name='info',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='address',
            field=models.CharField(blank=True, default='Jamcity', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sermon',
            name='preacher_profile_pic_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sermon',
            name='topic',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sermon',
            name='video_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
