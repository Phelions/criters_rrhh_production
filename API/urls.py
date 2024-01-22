
from django.urls import path, include
from rest_framework import routers
from API import views


router=routers.DefaultRouter()
router.register(r'usuario', views.UsuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include('rest_framework.urls', namespace='rest_framework'))
]

