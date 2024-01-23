from django.db import models

# Create your models here.

class Usuario(models.Model):
    rut = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.PositiveSmallIntegerField()
    correo = models.CharField(max_length=20)
    AREA = (
        ('RH', 'RRHH'),
        ('FN', 'FINANZAS'),
        ('VN', 'VENTAS'),
        ('BD', 'BODEGA'),
        ('PRD','PRODUCCION'),
    )
    area_desempenio = models.CharField(max_length=300, choices = AREA)
    estado = models.BooleanField(default=True)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    dias_Vacaciones = models.IntegerField()
    dias_Administrativos = models.IntegerField()
    fecha_contrato = models.DateField()
    fecha_termino_contrato = models.DateField()


## Podriamos una tabla login con usuario y contraseña y que se relacione con la tabla usuario, 
## para que no se pueda acceder a la tabla usuario sin antes pasar por la tabla login
    
    
    
    
## produccion , orden de requsicion, orden de producion 


class Login(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    contrasena = models.CharField(max_length=20)
    