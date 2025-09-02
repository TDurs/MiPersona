from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),  # ✅ aquí llamas a la vista index




    path('lista/',views.lista_documentos, name='lista_documentos'),

    path("documentos/", views.lista_documentos, name="lista_documentos"),
    path('subir/', views.subir_documento, name='subir_documento'),
    path('contactanos/', views.contactanos, name='contactanos'),
    path('contactos/', views.lista_contactos, name='lista_contactos'),
    path('pdfs/', views.lista_documentos, name='lista_documentos'),
]

