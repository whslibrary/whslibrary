# Generated by Django 4.2.3 on 2024-02-04 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("libpj", "0004_alter_profile_borrowed_alter_profile_on_time"),
    ]

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("Title", models.CharField(default="None", max_length=90)),
                ("id_book", models.IntegerField()),
                ("year", models.IntegerField()),
                ("description", models.CharField(default="None", max_length=400)),
                ("age_rating", models.CharField(default="None", max_length=40)),
                ("condition", models.CharField(default="None", max_length=90)),
                ("borrowed", models.IntegerField(blank=True, null=True)),
                ("pages", models.IntegerField(blank=True, null=True)),
                ("img", models.ImageField(default="", upload_to="img")),
            ],
        ),
    ]