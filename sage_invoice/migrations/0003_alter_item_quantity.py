# Generated by Django 5.1.2 on 2024-10-17 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sage_invoice", "0002_alter_invoice_template_choice"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="quantity",
            field=models.PositiveIntegerField(
                blank=True,
                db_comment="The quantity of the invoice item",
                help_text="The quantity of the item.",
                null=True,
                verbose_name="Quantity",
            ),
        ),
    ]
