from django.db import models

# Create your models here.
class Recording(models.Model):
    file = models.FileField(upload_to='recordings/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recording {self.id} at {self.uploaded_at}"