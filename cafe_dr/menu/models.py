from django.db import models


class MainMenuORM(models.Model):
    main_menu_item = models.CharField(max_length=50, db_index=True, unique=True)


class SubmenuORM(models.Model):
    submenu_item = models.CharField(max_length=50, db_index=True, unique=True)
    main_menu_item = models.ForeignKey("MainMenuORM", on_delete=models.CASCADE)


class DishRecipeORM(models.Model):
    dish = models.CharField(max_length=50, db_index=True, unique=True)
    dish_recipe = models.TextField(blank=True)
    submenu_item = models.ForeignKey("SubmenuORM", on_delete=models.CASCADE)
