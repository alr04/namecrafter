# Generated by Django 4.2.5 on 2024-11-21 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0003_alter_user_password_alter_user_username"),
    ]

    operations = [
        migrations.DeleteModel(name="User",),
    ]