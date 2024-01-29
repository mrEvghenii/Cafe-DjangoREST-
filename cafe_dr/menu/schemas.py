from ninja import ModelSchema

from .models import (
    MainMenuORM,
    SubmenuORM,
    DishRecipeORM,
)


# --- MainMenu ---
#
class MainMenu(ModelSchema):
    class Meta:
        model = MainMenuORM
        fields = "__all__"


class MainMenuCreate(ModelSchema):
    class Meta:
        model = MainMenuORM
        exclude = ["id"]

        class Config:
            extra = "forbid"


class MainMenuUpdatePatch(ModelSchema):
    class Meta:
        model = MainMenuORM
        exclude = ["id"]
        fields_optional = "__all__"

        class Config:
            extra = "forbid"


# --- Submenu ---
#
class Submenu(ModelSchema):
    class Meta:
        model = SubmenuORM
        fields = "__all__"


class SubmenuCreate(ModelSchema):
    class Meta:
        model = SubmenuORM
        exclude = ["id", "main_menu_item"]

        class Config:
            extra = "forbid"

    main_menu_item_id: int


class SubmenuUpdatePatch(ModelSchema):
    class Meta:
        model = SubmenuORM
        exclude = ["id", "main_menu_item"]
        fields_optional = "__all__"

        class Config:
            extra = "forbid"

    main_menu_item_id: int


# --- DishRecipe ---
#
class DishRecipe(ModelSchema):
    class Meta:
        model = DishRecipeORM
        fields = "__all__"


class DishRecipeCreate(ModelSchema):
    class Meta:
        model = DishRecipeORM
        exclude = ["id", "submenu_item"]

    class Config:
        extra = "forbid"

    submenu_item_id: int


class DishRecipeUpdatePatch(ModelSchema):
    class Meta:
        model = DishRecipeORM
        exclude = ["id", "submenu_item"]
        fields_optional = "__all__"

    class Config:
        extra = "forbid"

    submenu_item_id: int


# --- AllMenu ---
#
class SubmenuRel(Submenu):
    dishes: list["DishRecipe"] = []


class MenuRel(MainMenu):
    submenu_items: list["SubmenuRel"] = []
