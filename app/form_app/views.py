# Create your views here.
import os.path
import smtplib
import ssl
from email.header import Header
from email.message import EmailMessage
from email.utils import formataddr

from core.models import Form810, ProcedureAgreement, Form120, ApplicationInstruction, ReceptionEmail, AuthorizationRequest
from django.http import HttpResponse
from form_app.serializer import (Form810Serializer, ProcedureAgreementSerializer, Form120Serializer,
                                 AppInstructionSerializer, AuthRequestSerializer)
from form_filling import FormEightOneZero, ProcedureAgreementForm, AppInstructions,AuthorizationRequestForm
from rest_framework import status
from rest_framework.viewsets import ModelViewSet



def send_email(file_data, file_name):
    recpt_obj = ReceptionEmail.objects.first()
    msg = EmailMessage()
    msg['Subject'] = f'{file_name}'
    msg['From'] = formataddr((str(Header(recpt_obj.sender_name, 'utf-8')), recpt_obj.sender_email))
    msg['To'] = recpt_obj.receiver_email
    # msg.set_content('This is a test email from django API')
    msg.add_attachment(file_data, maintype='application',
                       subtype='octet-stream', filename=file_name)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        try:
            smtp.login(recpt_obj.sender_email, recpt_obj.sender_password)
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


class ProcedureAgreementView(ModelViewSet):
    def __init__(self, *args, **kwargs):
        super(ProcedureAgreementView, self).__init__(*args, **kwargs)
        self.app = ProcedureAgreementForm()

    serializer_class = ProcedureAgreementSerializer
    queryset = ProcedureAgreement.objects.all()

    def create(self, request, *args, **kwargs):
        print(request.data)
        output_path = self.app.write_to_file(request.data)
        file_pointer = open(output_path, 'rb').read()
        send_email(file_pointer, os.path.basename(output_path))
        # response = FileResponse(file_pointer, content_type='application/pdf')
        # response['Content-Disposition'] = 'attachment; filename=App_instructions.pdf'
        return HttpResponse('', status=status.HTTP_200_OK)


class Form810View(ModelViewSet):
    def __init__(self, *args, **kwargs):
        super(Form810View, self).__init__(*args, **kwargs)
        self.app = FormEightOneZero()

    serializer_class = Form810Serializer
    queryset = Form810.objects.all()

    def create(self, request, *args, **kwargs):
        output_path = self.app.write_to_file(request.data)
        file_pointer = open(output_path, 'rb').read()
        send_email(file_pointer, os.path.basename(output_path))
        # response = FileResponse(file_pointer, content_type='application/pdf')
        # response['Content-Disposition'] = 'attachment; filename=App_instructions.pdf'
        return HttpResponse('', status=status.HTTP_200_OK)


class AuthRequestView(ModelViewSet):
    def __init__(self, *args, **kwargs):
        super(AuthRequestView, self).__init__(*args, **kwargs)
        self.app = AuthorizationRequestForm()

    serializer_class = AuthRequestSerializer
    queryset = AuthorizationRequest.objects.all()

    def create(self, request, *args, **kwargs):
        output_path = self.app.write_to_file(request.data)
        print(request.data)
        file_pointer = open(output_path, 'rb').read()
        # send_email(file_pointer, os.path.basename(output_path))
        # response = FileResponse(file_pointer, content_type='application/pdf')
        # response['Content-Disposition'] = 'attachment; filename=App_instructions.pdf'
        return HttpResponse('', status=status.HTTP_200_OK)
