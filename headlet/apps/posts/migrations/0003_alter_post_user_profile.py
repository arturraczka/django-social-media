# Generated by Django 4.1.7 on 2023-03-11 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_profile_slug_alter_profile_user'),
        ('posts', '0002_remove_post_user_post_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user_profile',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_posts', to='profiles.profile'),
        ),
    ]
