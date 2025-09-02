from django.db import models

# Create your models here.

# Modelo para universidades
class Universidad(models.Model):
    nombre = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nombre


# Modelo para documentos en PDF
class Documento(models.Model):
    titulo = models.CharField(max_length=255)
    pdf = models.FileField(upload_to='pdfs/')  # se guardarán en MEDIA_ROOT/pdfs/
    fecha_subida = models.DateTimeField(auto_now_add=True)
    universidad = models.ForeignKey(Universidad, on_delete=models.CASCADE, related_name="documentos")

    def __str__(self):
        return f"{self.titulo} ({self.universidad})"
    
class Contacto(models.Model):
    nombre = models.CharField(max_length=150)
    gmail = models.EmailField()
    interes = models.TextField()
    fecha_solicitud = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.gmail}) - {self.fecha_solicitud.strftime('%d/%m/%Y %H:%M')}"