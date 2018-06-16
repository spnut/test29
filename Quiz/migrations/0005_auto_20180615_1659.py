# Generated by Django 2.0.1 on 2018-06-15 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0004_auto_20180615_1412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='ans',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='choice_text',
        ),
        migrations.AddField(
            model_name='question',
            name='ans',
            field=models.CharField(default=0, max_length=225),
        ),
        migrations.AddField(
            model_name='question',
            name='choice_text',
            field=models.CharField(default=0, max_length=200),
        ),
    ]