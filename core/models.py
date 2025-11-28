from django.db import models

class Persona(models.Model):
    class TipoDocumento(models.TextChoices):
        CEDULA = 'CC', 'Cédula de Ciudadanía'
        TARJETA_IDENTIDAD = 'TI', 'Tarjeta de Identidad'
        CEDULA_EXTRANJERIA = 'CE', 'Cédula de Extranjería'
        PASAPORTE = 'PAS', 'Pasaporte'
        OTRO = 'OTR', 'Otro'

    tipo_documento = models.CharField(
        max_length=3,
        choices=TipoDocumento.choices,
        default=TipoDocumento.CEDULA
    )
    # Usamos CharField para documento porque puede tener ceros a la izquierda o ser alfanumérico en pasaportes
    documento = models.CharField(max_length=20, unique=True) 
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    hobbie = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
        ordering = ['-created_at']
        # Buena práctica: Evitar duplicados compuestos si documento no fuera único globalmente
        # unique_together = ('tipo_documento', 'documento')

    def __str__(self):
        return f"{self.nombres} {self.apellidos} ({self.documento})"