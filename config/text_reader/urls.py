from django.urls import path
from .views import UploadFile, show_words


urlpatterns = [
    path('', UploadFile.as_view(), name='upload'),
    path('<int:text_file_id>/', show_words, name='show_words'),
]
