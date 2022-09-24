# Create your views here.
import datetime
import os.path
import smtplib
import ssl
from email.header import Header
from email.message import EmailMessage
from email.utils import formataddr

from core.models import ApplicationInstruction, Form120, ReceptionEmail
from django.http import HttpResponse
from django.utils import timezone
from form_app.serializer import AppInstructionSerializer, Form120Serializer
from form_filling import AppInstructions
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

def send_email(file_data, file_name):
    recpt_obj = ReceptionEmail.objects.first()
    msg = EmailMessage()
    msg['Subject'] = f'{file_name}'
    msg['From'] = formataddr((str(Header(recpt_obj.name, 'utf-8')), recpt_obj.email))
    msg['To'] = recpt_obj.email
    # msg.set_content('This is a test email from django API')
    msg.add_attachment(file_data, maintype='application',
                       subtype='octet-stream', filename=file_name)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        try:
            smtp.login(recpt_obj.email, recpt_obj.password)
            # smtp.login(recpt_obj.email, 'wpnlhstewnsbncnb')
            response = smtp.send_message(msg)


        except smtplib.SMTPResponseException as e:
            print(e)


class AppInstructView(ModelViewSet):
    def __init__(self, *args, **kwargs):
        super(AppInstructView, self).__init__(*args, **kwargs)
        self.app = AppInstructions()

    serializer_class = AppInstructionSerializer
    queryset = ApplicationInstruction.objects.all()

    def create(self, request, *args, **kwargs):
        output_path = self.app.read_write_first_page(request.data)
        file_pointer = open(output_path, 'rb').read()
        send_email(file_pointer, os.path.basename(output_path))
        # response = FileResponse(file_pointer, content_type='application/pdf')
        # response['Content-Disposition'] = 'attachment; filename=App_instructions.pdf'
        return HttpResponse('', status=status.HTTP_200_OK)


class Form120View(ModelViewSet):
    def __init__(self, *args, **kwargs):
        super(Form120View, self).__init__(*args, **kwargs)
        self.app = AppInstructions()

    serializer_class = Form120Serializer
    queryset = Form120.objects.all()

    def create(self, request, *args, **kwargs):
        output_path = self.app.read_write_first_page(request.data)
        file_pointer = open(output_path, 'rb').read()
        send_email(file_pointer, os.path.basename(output_path))
        # response = FileResponse(file_pointer, content_type='application/pdf')
        # response['Content-Disposition'] = 'attachment; filename=App_instructions.pdf'
        return HttpResponse('', status=status.HTTP_200_OK)
