from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from historial.models import Historial
from historial.serializers import HistorialSerializer


class RequestHistorial(APIView):
    @method_decorator(login_required(login_url='login.view.url'))
    def get(self, request, format=None):
        snippets = Historial.objects.all()
        serializer = HistorialSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HistorialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Answer": 1}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_302_FOUND)
