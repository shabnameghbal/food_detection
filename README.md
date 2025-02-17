Food Detection using YOLO and Django
Project Description
This is a Django-based web application that detects ingredients from an uploaded image using a YOLO (You Only Look Once) machine learning model. Based on the detected ingredients, the system suggests possible dishes. Additionally, users can save favorite dishes for easy access.
Features
Upload an image of ingredients
Detect ingredients using a trained YOLO model (best.pt)
Suggest dishes based on detected ingredients
Save and view favorite dishes
Project Structure
food_detection/               # Django project root  
│── food_detection/           # Main project settings  
│── image_processor/          # Django app for image processing  
│   │── templates/            # HTML templates  
│   │── static/               # Static files (CSS, JS)  
│   │── views.py              # Main logic for processing images and suggestions  
│   │── models.py             # Database models (UploadedImage, FavoriteDish)  
│   │── urls.py               # URL routes for the app  
│── ml_model/                 # Directory containing the trained YOLO model  
│── manage.py                 # Django management script  
│── db.sqlite3                # SQLite database  
│── requirements.txt          # Python dependencies  
│── .gitignore                # Files to be ignored by Git  
│── README.md                 # Project documentation  
Technologies Used
Python (Django Framework)
YOLOv8 (Ultralytics for ingredient detection)
SQLite (Database)
HTML/CSS (Frontend templates)
