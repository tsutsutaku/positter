# Generated by Django 3.0.5 on 2020-06-10 14:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('positterapp', '0009_post_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='post_id',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AddField(
            model_name='like',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='post',
            name='like_num',
            field=models.IntegerField(default=0),
        ),
    ]