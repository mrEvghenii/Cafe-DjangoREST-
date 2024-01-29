# Generated by Django 5.0.1 on 2024-01-25 16:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MainMenuORM",
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
                (
                    "main_menu_item",
                    models.CharField(db_index=True, max_length=50, unique=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SubmenuORM",
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
                (
                    "submenu_item",
                    models.CharField(db_index=True, max_length=50, unique=True),
                ),
                (
                    "main_menu_item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="menu.mainmenuorm",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DishRecipeORM",
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
                ("dish", models.CharField(db_index=True, max_length=50, unique=True)),
                ("dish_recipe", models.TextField()),
                (
                    "submenu_item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="menu.submenuorm",
                    ),
                ),
            ],
        ),
    ]