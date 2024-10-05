from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from Record.models import Recording
from .serializers import RecordingSerializer

class RecordingUpload(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        file_obj = request.data.get('audio_file')  # Use 'audio_file' as the key
        serializer = RecordingSerializer(data={'audio_file': file_obj})
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Recording uploaded successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, *args, **kwargs):
        recordings = Recording.objects.all()  # Optionally, you can filter results here
        serializer = RecordingSerializer(recordings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
