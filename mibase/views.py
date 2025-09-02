from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Documento, Contacto
from .forms import DocumentoForm, ContactoForm
from django.core.paginator import Paginator
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import JsonResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')

def hello(request):
    return HttpResponse("Hello, world. You're at the mibase index.")

@xframe_options_exempt
def subir_documento(request):
    if request.method == "POST":
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("lista_documentos")
    else:
        form = DocumentoForm()
    return render(request, "subir_documento.html", {"form": form})

@xframe_options_exempt 
def lista_documentos(request):
    documentos = Documento.objects.all().order_by("-fecha_subida")
    paginator = Paginator(documentos, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "partials/documentos_list.html", {"page_obj": page_obj})



@xframe_options_exempt
def contactanos(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"success": True})
            return redirect("lista_contactos")
        else:
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"success": False, "errors": form.errors})
    else:
        form = ContactoForm()
    return render(request, "contactanos.html", {"form": form})

@xframe_options_exempt
def lista_contactos(request):
    contactos = Contacto.objects.all().order_by("-fecha_solicitud")
    return render(request, "lista_contactos.html", {"contactos": contactos})

