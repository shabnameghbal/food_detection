import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ImageUploadForm
from .models import UploadedImage, FavoriteDish  # Import models
from urllib.parse import unquote
from ultralytics import YOLO

# Load the YOLO model
MODEL_PATH = os.path.join(settings.BASE_DIR, "ml_model", "best.pt")
model = YOLO(MODEL_PATH)

def home(request):
    """Displays only the upload form."""
    form = ImageUploadForm()
    return render(request, "image_processor/home.html", {"form": form})

def upload_image(request):
    """Handles image upload and redirects to success page with image URL."""
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.save()
            success_url = reverse("upload_success") + f"?image_url={uploaded_image.image.url}"
            return redirect(success_url)
    else:
        form = ImageUploadForm()
    return render(request, "image_processor/home.html", {"form": form})

def upload_success(request):
    """Displays the success page with the uploaded image."""
    image_url = request.GET.get("image_url", "")
    return render(request, "image_processor/upload_success.html", {"image_url": image_url})

def detect_ingredients(request):
    """Detects ingredients and redirects to suggest_dishes."""
    image_url = request.GET.get("image_url", "").replace(settings.MEDIA_URL, "", 1)
    image_path = os.path.join(settings.MEDIA_ROOT, image_url.replace("/", os.sep))

    if not os.path.exists(image_path):
        return render(request, "image_processor/error.html", {"error_message": f"File not found: {image_path}"})

    # Run YOLO model
    results = model(image_path)
    ingredients = list(set(model.names[int(cls)] for r in results for cls in r.boxes.cls))

    # Redirect to suggest_dishes page
    ingredients_param = ",".join(ingredients)
    results_url = reverse("suggest_dishes") + f"?image_url={request.GET.get('image_url', '')}&ingredients={ingredients_param}"
    return redirect(results_url)

def suggest_dishes(request):
    """Suggests dishes based on detected ingredients."""
    image_url = request.GET.get("image_url", "")
    ingredient_list = request.GET.get("ingredients", "").split(",")

    # Placeholder for dish suggestions
    suggested_dishes = {
        "egg": ["Omelette", "Scrambled Eggs"],
        "onion": ["Onion Soup", "Grilled Onion"],
        "garlic": ["Garlic Bread", "Garlic Butter Chicken"],
    }

    dishes = set()
    for ingredient in ingredient_list:
        dishes.update(suggested_dishes.get(ingredient, []))

    return render(request, "image_processor/suggest_dishes.html", {
        "image_url": image_url,
        "ingredients": ingredient_list,
        "dishes": list(dishes),
    })

def save_favorite_dish(request):
    """Saves a dish to the session-based favorites list."""
    if request.method == "POST":
        dish_name = request.POST.get("dish_name")
        if dish_name:
            if "favorites" not in request.session:
                request.session["favorites"] = []
            if dish_name not in request.session["favorites"]:
                request.session["favorites"].append(dish_name)
                request.session.modified = True  # Ensure session updates
    return redirect("favorites_list")

def favorites_list(request):
    """Displays session-based favorite dishes."""
    favorites = request.session.get("favorites", [])
    return render(request, "image_processor/favorites_list.html", {"favorites": favorites})

