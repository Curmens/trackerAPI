# Generated by Django 4.1.4 on 2022-12-18 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_rename_firstname_user_firstname_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="userStatus",
            field=models.IntegerField(default=0),
        ),
    ]
