from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import InfoSerializer
from datetime import datetime
import pytz

class InfoAPIView(APIView):
    def get(self, request):
        data = {
            "email": "ekponsikan01@gmail.com",  # registered email
            "current_datetime": datetime.now(pytz.utc).isoformat(),
            "github_url": "https://github.com/Nsikanekpo/hng12_api.git"  # my repo URL
        }
        serializer = InfoSerializer(data)
        return Response(serializer.data)

