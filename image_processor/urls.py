from django.urls import path
from .views import home, upload_image, upload_success, detect_ingredients, suggest_dishes, save_favorite_dish, favorites_list


urlpatterns = [
    path("", home, name="home"),
    path("upload/", upload_image, name="upload_image"),
    path("upload-success/", upload_success, name="upload_success"),
    path("detect-ingredients/", detect_ingredients, name="detect_ingredients"),
    path("suggest-dishes/", suggest_dishes, name="suggest_dishes"),
    path("save-favorite/", save_favorite_dish, name="save_favorite_dish"),
    path("favorites/", favorites_list, name="favorites_list"),
]

