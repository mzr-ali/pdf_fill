# Create your views here.
from django.http import FileResponse
from form_app.serializer import AppInstructionSerializer
from rest_framework import status
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

#
# @action(methods=['POST'], detail=AppInstructionSerializer, url_path='app_instructions')
# @api_view(['POST'])
# def AppInstructView(request, pk=None):
#     serializer = AppInstructionSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
from form_filling import AppInstructions


# class AppInstructView(RetrieveModelMixin, CreateModelMixin, GenericViewSet):
#     serializer_class = AppInstructionSerializer()
#
#     def __init__(self, *args, **kwargs):
#         super(AppInstructView, self).__init__(*args, **kwargs)
#         self.app = AppInstructions()
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         output_path = self.app.read_write_first_page(request.data)
#         file_pointer = open(output_path, 'rb')
#         response = Response(file_pointer, content_type='application/pdf')
#         response['Content-Disposition'] = 'attachment; filename=App_instructions.pdf'
#         return response

#
class AppInstructView(GenericViewSet, CreateModelMixin):
    def __init__(self, *args, **kwargs):
        super(AppInstructView, self).__init__(*args, **kwargs)
        self.app = AppInstructions()
    serializer_class = AppInstructionSerializer

    def create(self, request, *args, **kwargs):
        output_path = self.app.read_write_first_page(request.data)
        file_pointer = open(output_path, 'rb')
        response = FileResponse(file_pointer,  content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=App_instructions.pdf'
        return response

    # def post(self, request, *args, **kwargs):
    #     print(request.data)
    #     output_path = self.app.read_write_first_page(request.data)
    #
    #     file_pointer = open(output_path, 'rb')
    #     response = Response(file_pointer, status=status.HTTP_200_OK)
    #     response['Content-Disposition'] = 'attachment; filename=App_instructions.pdf'
    #     return response
