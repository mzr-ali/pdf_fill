from django.urls import path, include

from rest_framework import routers

from form_app.views import (
    AppInstructView,
    Form120View,
    Form810View,
    ProcedureAgreementView,
    AuthRequestView,
    Form248View,
    CheckListView,
ExceptionListView,
Form244View
)

router = routers.DefaultRouter()
router.register(r'app_instruction', AppInstructView, basename='app_instruct')
router.register(r'form_120', Form120View, basename='form120')
router.register(r'procedure_agreement', ProcedureAgreementView, basename='procedure_agree')
router.register(r'form_810', Form810View, basename='form_810')
router.register(r'authorization_request', AuthRequestView, basename='authorization_request')
router.register(r'form_248', Form248View, basename='form_248')
router.register(r'check_list_form', CheckListView, basename='checklist_form')
router.register(r'exception_list', ExceptionListView, basename='exception_list')
router.register(r'form_244', Form244View, basename='form_244')
app_name = 'filling'
# from form_app.views import AppInstructView
urlpatterns = [
    path('', include(router.urls))
]