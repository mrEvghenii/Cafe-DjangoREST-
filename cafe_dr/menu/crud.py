from django.shortcuts import get_object_or_404

from menu.models import (
    MainMenuORM,
    SubmenuORM,
    DishRecipeORM,
)

from menu.schemas import (
    MainMenuCreate,
    MainMenuUpdatePatch,
    SubmenuCreate,
    SubmenuUpdatePatch,
    DishRecipeCreate,
    DishRecipeUpdatePatch,
)


def get_entries(
    model_orm: MainMenuORM | SubmenuORM | DishRecipeORM,
    request,
):
    obj = model_orm.objects.all()
    return obj


def create_entry(
    model_orm: MainMenuORM | SubmenuORM | DishRecipeORM,
    obj_in: MainMenuCreate | SubmenuCreate | DishRecipeCreate,
    request,
):
    obj = model_orm.objects.create(**obj_in.dict())
    return obj


def get_entry(
    model_orm: MainMenuORM | SubmenuORM | DishRecipeORM,
    obj_id: int,
    request,
):
    obj = get_object_or_404(model_orm, id=obj_id)
    return obj


def update_entry(
    model_orm: MainMenuORM | SubmenuORM | DishRecipeORM,
    obj_id: int,
    obj_update: MainMenuUpdatePatch | SubmenuUpdatePatch | DishRecipeUpdatePatch,
    request,
):
    obj = get_object_or_404(model_orm, id=obj_id)
    for name, value in obj_update.model_dump(exclude_unset=True).items():
        setattr(obj, name, value)
    obj.save()
    return obj


def delete_entry(
    model_orm: MainMenuORM | SubmenuORM | DishRecipeORM,
    obj_id: int,
    request,
):
    obj = get_object_or_404(model_orm, id=obj_id)
    obj.delete()
