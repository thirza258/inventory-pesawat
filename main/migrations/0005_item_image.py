# Generated by Django 4.2.5 on 2023-10-03 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_item_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="image",
            field=models.URLField(blank=True, null=True),
        ),
    ]
