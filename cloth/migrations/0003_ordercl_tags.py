# Generated by Django 4.2.6 on 2023-11-13 14:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cloth", "0002_remove_customercl_name_remove_ordercl_order_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="ordercl",
            name="tags",
            field=models.ManyToManyField(to="cloth.tagcl"),
        ),
    ]
