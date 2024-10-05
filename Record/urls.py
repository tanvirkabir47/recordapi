from django.urls import path
from .views import RecordingUpload

urlpatterns = [
    path('upload/', RecordingUpload.as_view(), name='upload-recording'),
]