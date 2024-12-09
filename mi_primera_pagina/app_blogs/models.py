from django.db import models

# Create your models here.

class Blog(models.Model):
    
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    contenido = models.CharField(max_length=10000)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.autor} - {self.fecha_publicacion}"
    
