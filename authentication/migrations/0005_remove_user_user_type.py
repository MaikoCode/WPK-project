# Generated by Django 4.2.3 on 2023-07-12 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0004_alter_user_role_alter_user_user_type"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="user_type",
        ),
    ]
