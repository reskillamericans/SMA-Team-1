# Generated by Django 3.2.5 on 2021-07-16 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smapp', '0006_merge_0002_auto_20210712_0800_0005_auto_20210703_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='password_resets',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='password_resets',
            name='is_token_used',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='password_resets',
            name='token',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='password_resets',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]