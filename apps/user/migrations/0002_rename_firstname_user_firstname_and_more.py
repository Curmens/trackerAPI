# Generated by Django 4.1.4 on 2022-12-18 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="firstname",
            new_name="firstName",
        ),
        migrations.RenameField(
            model_name="user",
            old_name="lastname",
            new_name="lastName",
        ),
        migrations.AddField(
            model_name="user",
            name="userStatus",
            field=models.BooleanField(default=False),
        ),
    ]