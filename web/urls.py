from django.urls import path
from . import views
from .views import index, CustomLoginView, CustomLogoutView,RegisterView, arrendar, misArriendos,retornar,devolver, reporteArriendos
urlpatterns = [
    path('', index, name='index'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/register/', RegisterView.as_view(), name='register'),
    path('account/logout/', CustomLogoutView.as_view(), name='logout'),
    path('videojuego/<id>/arrendar/', arrendar, name='arrendar'),
    path('mis_arriendos/', misArriendos, name='mis_arriendos'),
    path('videojuego/<int:id>/retornar/', retornar, name='retornar'),
    path('arriendos/<int:id>/devolver', devolver, name='devolver'),
    path('reporte_arriendos/', reporteArriendos, name='reporte_arriendos'),
 
]