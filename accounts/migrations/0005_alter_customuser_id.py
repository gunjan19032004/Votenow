# Generated by Django 5.1.1 on 2024-09-26 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_auto_20201226_2340"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
