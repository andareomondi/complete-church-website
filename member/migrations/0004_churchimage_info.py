# Generated by Django 5.1.1 on 2024-12-27 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_remove_sermon_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='churchimage',
            name='info',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]