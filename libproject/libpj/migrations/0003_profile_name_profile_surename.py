# Generated by Django 4.2.3 on 2024-02-02 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("libpj", "0002_alter_profile_trust"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="name",
            field=models.CharField(default="None", max_length=40),
        ),
        migrations.AddField(
            model_name="profile",
            name="surename",
            field=models.CharField(default="None", max_length=40),
        ),
    ]
