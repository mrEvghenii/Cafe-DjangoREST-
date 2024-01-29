from ninja import NinjaAPI
from menu.api import router as menu_router

api = NinjaAPI()

api.add_router("menu/", menu_router)
