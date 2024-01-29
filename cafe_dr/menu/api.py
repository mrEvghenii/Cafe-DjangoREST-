from django.http import HttpResponse
from ninja import Router

from menu.models import MainMenuORM, SubmenuORM, DishRecipeORM
from menu.schemas import (
    MainMenu,
    MainMenuCreate,
    MainMenuUpdatePatch,
    Submenu,
    SubmenuCreate,
    SubmenuUpdatePatch,
    DishRecipe,
    DishRecipeCreate,
    DishRecipeUpdatePatch,
)

from menu import crud
from menu import insert_test_data as itd


router = Router()

MM = ["Main Menu"]
SM = ["Submenu"]
DR = ["Dishes and Recipes"]

MM_path = "/main_menu"
SM_path = "/submenu"
DR_path = "/dish_recipe"


#  --- Insert tst data ---
@router.get("/itd", tags=["Insert test data"])
def insert_test_data(request):
    itd.insert_test_data()
    return HttpResponse("Test data added", status=201)


# --- Main Menu ---
@router.get(MM_path, response=list[MainMenu], tags=MM)
def get_main_menu_items(request):
    return crud.get_entries(
        request=request,
        model_orm=MainMenuORM,
    )


@router.post(
    MM_path,
    response=MainMenu,
    tags=MM,
)
def create_main_menu_item(
    request,
    menu_in: MainMenuCreate,
):
    return crud.create_entry(
        request=request,
        model_orm=MainMenuORM,
        obj_in=menu_in,
    )


@router.get(MM_path + "/{menu_id}/", response=MainMenu, tags=MM)
def get_main_menu_item(request, menu_id: int):
    return crud.get_entry(
        request=request,
        model_orm=MainMenuORM,
        obj_id=menu_id,
    )


@router.patch(MM_path + "/{menu_id}/", response=MainMenu, tags=MM)
def update_main_menu_item(
    request,
    menu_id: int,
    menu_update: MainMenuUpdatePatch,
):
    return crud.update_entry(
        request=request,
        model_orm=MainMenuORM,
        obj_update=menu_update,
        obj_id=menu_id,
    )


@router.delete(MM_path + "/{menu_id}/", tags=MM)
def delete_main_menu_item(request, menu_id: int):
    return crud.delete_entry(
        request=request,
        model_orm=MainMenuORM,
        obj_id=menu_id,
    )


# --- Submenu ---
@router.get(SM_path, response=list[Submenu], tags=SM)
def get_submenu_items(request):
    return crud.get_entries(
        request=request,
        model_orm=SubmenuORM,
    )


@router.post(SM_path, response=Submenu, tags=SM)
def create_submenu_item(
    request,
    submenu_in: SubmenuCreate,
):
    return crud.create_entry(
        request=request,
        model_orm=SubmenuORM,
        obj_in=submenu_in,
    )


@router.get(SM_path + "/{submenu_id}/", response=Submenu, tags=SM)
def get_submenu_item(request, submenu_id: int):
    return crud.get_entry(
        request=request,
        model_orm=SubmenuORM,
        obj_id=submenu_id,
    )


@router.patch(SM_path + "/{submenu_id}/", response=Submenu, tags=SM)
def update_submenu_item(
    request,
    submenu_id: int,
    submenu_update: SubmenuUpdatePatch,
):
    return crud.update_entry(
        request=request,
        model_orm=SubmenuORM,
        obj_update=submenu_update,
        obj_id=submenu_id,
    )


@router.delete(SM_path + "/{submenu_id}/", tags=SM)
def delete_submenu_item(request, submenu_id: int):
    return crud.delete_entry(
        request=request,
        model_orm=SubmenuORM,
        obj_id=submenu_id,
    )


# --- Dishes and Recipes ---
@router.get(DR_path, response=list[DishRecipe], tags=DR)
def get_dish_recipe_items(request):
    return crud.get_entries(
        request=request,
        model_orm=DishRecipeORM,
    )


@router.post(DR_path, response=DishRecipe, tags=DR)
def create_dish_recipe_item(
    request,
    dr_in: DishRecipeCreate,
):
    return crud.create_entry(
        request=request,
        model_orm=DishRecipeORM,
        obj_in=dr_in,
    )


@router.get(DR_path + "/{dish_recipe_id}/", response=DishRecipe, tags=DR)
def get_dish_recipe_item(request, dish_recipe_id: int):
    return crud.get_entry(
        request=request,
        model_orm=DishRecipeORM,
        obj_id=dish_recipe_id,
    )


@router.patch(DR_path + "/{dish_recipe_id}/", response=DishRecipe, tags=DR)
def update_dish_recipe_item(
    request,
    dish_recipe_id: int,
    dish_recipe_update: DishRecipeUpdatePatch,
):
    return crud.update_entry(
        request=request,
        model_orm=DishRecipeORM,
        obj_update=dish_recipe_update,
        obj_id=dish_recipe_id,
    )


@router.delete(DR_path + "/{dish_recipe_id}/", tags=DR)
def delete_dish_recipe_item(request, dish_recipe_id: int):
    return crud.delete_entry(
        request=request,
        model_orm=DishRecipeORM,
        obj_id=dish_recipe_id,
    )
