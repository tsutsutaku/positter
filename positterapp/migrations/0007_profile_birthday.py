# Generated by Django 3.0.5 on 2020-06-09 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('positterapp', '0006_auto_20200609_0419'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]
