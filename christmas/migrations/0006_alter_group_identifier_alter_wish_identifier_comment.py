# Generated by Django 4.2.4 on 2023-08-17 13:54

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("christmas", "0005_group_identifier_wish_identifier"),
    ]

    operations = [
        migrations.AlterField(
            model_name="group",
            name="identifier",
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name="wish",
            name="identifier",
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.CreateModel(
            name="Comment",
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
                ("content", models.TextField(max_length=512)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="christmas.user"
                    ),
                ),
                (
                    "wish",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="christmas.wish"
                    ),
                ),
            ],
        ),
    ]
