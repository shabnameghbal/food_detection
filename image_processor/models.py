from django.db import models

class UploadedImage(models.Model):
    image = models.ImageField(upload_to="uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id} uploaded at {self.uploaded_at}"



class FavoriteDish(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

