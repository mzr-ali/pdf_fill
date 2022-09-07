# Create your views here.
from core.models import ApplicationInstruction, Form120
from django.http import FileResponse
from form_app.serializer import AppInstructionSerializer, Form120Serializer
from form_filling import AppInstructions
from rest_framework.viewsets import ModelViewSet



class AppInstructView(ModelViewSet):
    def __init__(self, *args, **kwargs):
        super(AppInstructView, self).__init__(*args, **kwargs)
        self.app = AppInstructions()

    serializer_class = AppInstructionSerializer
    queryset = ApplicationInstruction.objects.all()

    def create(self, request, *args, **kwargs):
        output_path = self.app.read_write_first_page(request.data)
        file_pointer = open(output_path, 'rb')
        response = FileResponse(file_pointer, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=App_instructions.pdf'
        return response


class Form120View(ModelViewSet):
    def __init__(self, *args, **kwargs):
        super(Form120View, self).__init__(*args, **kwargs)
        self.app = AppInstructions()

    serializer_class = Form120Serializer
    queryset = Form120.objects.all()

    def create(self, request, *args, **kwargs):
        output_path = self.app.read_write_first_page(request.data)
        file_pointer = open(output_path, 'rb')
        response = FileResponse(file_pointer, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=App_instructions.pdf'
        return response
