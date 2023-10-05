from django.db import models
 
from .opciones import si_no,entidades, nacionalidad, origen, sector, sexo, tipo_paciente, resultado

class estados(models.Model):
    clave = models.CharField(max_length=2,primary_key=True)
    estado = models.CharField(max_length=30)

class municipios(models.Model):
    clave = models.CharField(primary_key=True, max_length=3)
    municipio = models.CharField(max_length=30)
    clave_estado = models.ForeignKey(estados,on_delete=models.CASCADE, default='99')


class setDatos(models.Model):
    FECHA_ACTUALIZACION = models.DateField(auto_now_add=True, null=True)
    ID_REGISTRO = models.CharField(max_length=20,primary_key=True)
    ORIGEN = models.CharField(max_length=2, choices=origen, default='99')
    SECTOR = models.CharField(max_length=2, choices=sector, default='99')
    ENTIDAD_UM = models.CharField(max_length=2,choices=entidades,default='99',null=True)
    SEXO = models.CharField(max_length=2,choices=sexo,default='99')
    ENTIDAD_NAC = models.CharField(max_length=2,choices=entidades,default='99')
    ENTIDAD_RES = models.ForeignKey(estados,on_delete=models.CASCADE,default='99',null=True)
    MUNICIPIO_RES = models.ForeignKey(municipios,on_delete=models.CASCADE,default='99',null=True)
    TIPO_PACIENTE = models.CharField(max_length=2,choices=tipo_paciente,default='99')
    FECHA_INGRESO = models.DateField(null=True)
    FECHA_SINTOMAS = models.DateField(null=True)
    FECHA_DEF = models.DateField(null=True)
    INTUBADO = models.CharField(max_length=2, choices=si_no, default='1')
    NEUMONIA = models.CharField(max_length=2, choices=si_no, default='1')
    EDAD = models.IntegerField(null=True)
    NACIONALIDAD = models.CharField(max_length=2,choices=nacionalidad,default='99')
    EMBARAZO = models.CharField(max_length=2, choices=si_no, default='1')
    HABLA_LENGUA_INDIG = models.CharField(max_length=2, choices=si_no, default='1')
    DIABETES = models.CharField(max_length=2, choices=si_no, default='1')
    EPOC = models.CharField(max_length=2, choices=si_no, default='1')
    ASMA = models.CharField(max_length=2, choices=si_no, default='1')
    INMUSUPR = models.CharField(max_length=2, choices=si_no, default='1')
    HIPERTENSION = models.CharField(max_length=2, choices=si_no, default='1')
    OTRA_COM = models.CharField(max_length=2, choices=si_no, default='1')
    CARDIOVASCULAR = models.CharField(max_length=2, choices=si_no, default='1')
    OBESIDAD = models.CharField(max_length=2, choices=si_no, default='1')
    RENAL_CRONICA = models.CharField(max_length=2, choices=si_no, default='1')
    TABAQUISMO = models.CharField(max_length=2, choices=si_no, default='1')
    OTRO_CASO = models.CharField(max_length=2, choices=si_no, default='1')
    RESULTADO = models.CharField(max_length=2, choices=resultado, default='1')
    MIGRANTE = models.CharField(max_length=2, choices=si_no, default='1')
    PAIS_NACIONALIDAD = models.CharField(max_length=20,null=True)
    PAIS_ORIGEN = models.CharField(max_length=2,choices=nacionalidad,default='99')
    UCI = models.CharField(max_length=2, choices=si_no, default='1')
