# Generated by Django 3.2.4 on 2021-06-28 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smapp', '0002_alter_user_socials_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='comments_count',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='likes_count',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='followers_count',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='following_count',
            field=models.IntegerField(default=0, null=True),
        ),
    ]