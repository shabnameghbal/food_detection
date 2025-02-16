from ultralytics import YOLO
from django.conf import settings

# Load the trained YOLO model
model = YOLO(str(settings.ML_MODEL_PATH))
