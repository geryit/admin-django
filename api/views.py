from rest_framework.views import APIView
from rest_framework.response import Response
from work.models import Work
from work.serializers import WorkSerializer  # You need to create this serializer


class WorkList(APIView):
    def get(self, request, format=None):
        all_works = Work.objects.all()
        serializer = WorkSerializer(all_works, many=True)
        return Response(serializer.data)