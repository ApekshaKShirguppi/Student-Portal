# Generated by Django 4.1.2 on 2023-04-14 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_staff_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff_notification',
            name='status',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
