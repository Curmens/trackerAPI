# Generated by Django 4.1.4 on 2022-12-18 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0005_alter_user_managers"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="is_superuser",
            field=models.BooleanField(default=False),
        ),
    ]
