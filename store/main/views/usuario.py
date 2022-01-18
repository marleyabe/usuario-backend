from distutils import extension
from urllib import request
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from main.models import Usuario
from main.serializers import UsuarioSerializer

from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class UsuarioViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'delete', 'post', 'put']

    queryset = Usuario.objects.all()

    serializer_class = UsuarioSerializer



    def create(self, request):
        try:
            __accept_extensions = ['pdf', 'png', 'jpeg', 'jpg']

            serializer = self.get_serializer(data=request.data)
            print(request.data)
            __extension = str(request.data['file']).split(".")
            if  __extension[1] in __accept_extensions:
                print("tá dentro",__extension)


                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
            else:
                serializer.is_valid(raise_exception=False)
                return Response("arquivo não suportado", status=status.HTTP_400_BAD_REQUEST)
            headers = self.get_success_headers(serializer.data)

            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except IndexError:
            
            __extension = "error.pdf"
            return Response("coloque o arquivo", status=status.HTTP_400_BAD_REQUEST)