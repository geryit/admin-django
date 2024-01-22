# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response

from work.models import Work
from .serializers import WorkSerializer

@api_view(['GET'])
def index(request):
    works = Work.objects.all()
    serializer = WorkSerializer(works, many=True)
    return Response(serializer.data)
