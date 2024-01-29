from django.http import HttpResponse

from menu.models import (
    MainMenuORM,
    SubmenuORM,
    DishRecipeORM,
)


def insert_main_menu():
    a1 = MainMenuORM.objects.create(main_menu_item="Главные блюда")
    a2 = MainMenuORM.objects.create(main_menu_item="Вторые блюда")
    a3 = MainMenuORM.objects.create(main_menu_item="Напитки")


def insert_submenu():
    a4 = SubmenuORM.objects.create(main_menu_item_id=1, submenu_item="Супы")
    a5 = SubmenuORM.objects.create(main_menu_item_id=1, submenu_item="Роллы")
    a6 = SubmenuORM.objects.create(main_menu_item_id=2, submenu_item="Салаты")
    a7 = SubmenuORM.objects.create(
        main_menu_item_id=3, submenu_item="Алкогольные напитки"
    )
    a8 = SubmenuORM.objects.create(
        main_menu_item_id=3, submenu_item="Безалкогольные напитки"
    )


def insert_dish_recipes():
    a10 = DishRecipeORM.objects.create(
        submenu_item_id=2, dish="Ролл Калифорния", dish_recipe="Рецепт неизвестен"
    )
    a11 = DishRecipeORM.objects.create(
        submenu_item_id=3, dish="Прошутто с микс салатом и моцареллой"
    )
    a12 = DishRecipeORM.objects.create(submenu_item_id=4, dish="Алкогольный Махито")
    a13 = DishRecipeORM.objects.create(submenu_item_id=5, dish="Безалкогольный Махито")
    a14 = DishRecipeORM.objects.create(submenu_item_id=5, dish="Лимонад")


def insert_test_data():
    insert_main_menu()
    insert_submenu()
    insert_dish_recipes()
    print("Добавлены тестовые данные в таблицы")
