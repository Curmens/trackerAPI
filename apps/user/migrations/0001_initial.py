# Generated by Django 4.1.4 on 2022-12-18 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=255, unique=True, verbose_name="email address"
                    ),
                ),
                ("firstname", models.CharField(max_length=50)),
                ("lastname", models.CharField(max_length=50)),
                (
                    "username",
                    models.CharField(
                        blank=True, max_length=30, verbose_name="username"
                    ),
                ),
                ("is_active", models.BooleanField(default=False)),
                ("is_admin", models.BooleanField(default=False)),
                ("phone", models.CharField(max_length=20)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
