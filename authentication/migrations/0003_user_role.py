# Generated by Django 4.0.6 on 2023-07-12 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_user_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('USER', 'user'), ('SUPPLIER', 'supplier')], default='USER', max_length=30, verbose_name='Rôle'),
            preserve_default=False,
        ),
    ]
