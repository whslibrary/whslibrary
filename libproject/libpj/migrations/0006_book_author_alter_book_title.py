# Generated by Django 4.2.3 on 2024-02-06 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("libpj", "0005_book"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="author",
            field=models.CharField(default="None", max_length=40),
        ),
        migrations.AlterField(
            model_name="book",
            name="Title",
            field=models.CharField(default="None", max_length=100),
        ),
    ]