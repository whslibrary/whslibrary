# Generated by Django 4.2.3 on 2024-02-02 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("libpj", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="trust",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
