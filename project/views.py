from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Project

from .serializers import ProjectSerializer


class LatestProjectsList(APIView):
    def get(self, request, format=None):
        products = Project.objects.all()[0:4]
        serializer = ProjectSerializer(products, many=True)
        return Response(serializer.data)
