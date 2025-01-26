from django.db import models

# Create your models here.

marcas = (('Fiat', 'Fiat'), ('Chevrolet', 'Chevrolet'), ('Ford', 'Ford'), ('Toyota', 'Toyota'))

categoria = (('particular', 'Particular'), ('carga', 'Carga'), ('transporte', 'Transporte'))

class Vehiculo(models.Model):
    marca = models.CharField(max_length=20,choices=marcas,default='Ford')
    modelo = models.CharField(max_length=100, verbose_name='Modelo')
    serialCarroceria = models.CharField(max_length=50, verbose_name='Serial Carroceria')
    serialMotor = models.CharField(max_length=50, verbose_name='Serial Motor')
    categoria = models.CharField(max_length=20, choices=categoria, default='particular')
    precio = models.IntegerField()
    fechaCreacion = models.DateField(auto_now_add=True)
    fechaModificacion = models.DateField(auto_now=True)

    class Meta:
        permissions = [
            ("add_vehiculomodel", "Puede agregar vehiculos"),
        ]

    def __str__(self):
        return f'{self.marca} {self.modelo} {self.serialCarroceria}'

    @property
    def condicion_precio(self):
        if self.precio <= 10000:
            return 'Bajo'
        elif self.precio <= 30000:
            return 'Medio'
        else:
            return 'Alto'