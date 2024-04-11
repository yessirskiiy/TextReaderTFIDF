from django.db import models


class TextFile(models.Model):
    file = models.FileField(upload_to='files/')
    loaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
