from django.urls import path, include

from form_app.views import AppInstructView
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'app_instruction', AppInstructView, basename='app_instruct')
app_name = 'filling'
# from form_app.views import AppInstructView
urlpatterns = [
    path('', include(router.urls) )
]