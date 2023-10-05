from datetime import date
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import setDatos


TEMPLATE_DIRS = {
    'os.path.join(BASE_DIR,"templates")'
}

def index(request):
    return render(request, "index.html")

def listar(request):
    alldata = setDatos.objects.all()
    datos = {'setDatos' : alldata}
    return render(request, "crud_datos/listar.html", datos)

def agregar(request):
    if request.method=='POST':
        if request.POST.get('fechaact') and request.POST.get('idregistro') and request.POST.get('EntidadNac') and request.POST.get('EntidadUM') and request.POST.get('entidad_res_id') and request.POST.get('fecha_ingreso') and request.POST.get('fecha_Sintomas') and  request.POST.get('fecha_def') and request.POST.get('intubado') and request.POST.get('neumonia') and request.POST.get('edad') and request.POST.get('nacionalidad') and  request.POST.get('embarazo') and request.POST.get('habla_lengua_indigena') and request.POST.get('diabetes') and request.POST.get('epoc') and request.POST.get('asma') and request.POST.get('inmusupr') and request.POST.get('otra_com') and request.POST.get('cardiovascular') and request.POST.get('obesidad') and request.POST.get('renal cronica') and request.POST.get('tabaquismo') and  request.POST.get('otro_caso') and request.POST.get('resultado') and request.POST.get('migrante') and request.POST.get('Pais_Nacionalidad') and request.POST.get('pais_origen') and request.POST.get('uci') and request.POST.get('municipio_res_id') and request.POST.get('origen') and request.POST.get('sector') and request.POST.get('sexo') and request.POST.get('tipo_paciente'):
            registro = setDatos()
            registro.fechaact = request.POST.get('registro.fechaact')
            registro.idregistro = request.POST.get('registro.idregistro')
            registro.EntidadNac = request.POST.get('registro.EntidadNac')
            registro.EntidadUM = request.POST.get('registro.EntidadUM')
            registro.entidad_res_id = request.POST.get('registro.entidad_res_id')
            registro.fecha_ingreso = request.POST.get('registro.fecha_ingreso')
            registro.fecha_Sintomas = request.POST.get('registro.fecha_Sintomas')
            registro.fecha_def = request.POST.get('registro.fecha_def')
            registro.intubado = request.POST.get('registro.intubado')
            registro.neumonia = request.POST.get('registro.neumonia')
            registro.edad = request.POST.get('registro.edad')
            registro.nacionalidad = request.POST.get('registro.nacionalidad')
            registro.embarazo = request.POST.get('registro.embarazo')
            registro.habla_lengua_indigena = request.POST.get('registro.habla_lengua_indigena')
            registro.diabetes = request.POST.get('registro.diabetes')
            registro.epoc = request.POST.get('registro.epoc')
            registro.asma = request.POST.get('registro.asma')
            registro.inmunosupr = request.POST.get('registro.inmunosupr')
            registro.otra_com = request.POST.get('registro.otra_com')
            registro.cardiovascular = request.POST.get('registro.cardiovascular')
            registro.obesidad = request.POST.get('registro.obesidad')
            registro.renal_cronica = request.POST.get('registro.renal cronica')
            registro.tabaquismo = request.POST.get('registro.tabaquismo')
            registro.otro_caso = request.POST.get('registro.otro_caso')
            registro.resultado = request.POST.get('registro.resultado')
            registro.migrante = request.POST.get('registro.migrante')
            registro.Pais_Nacionalidad = request.POST.get('registro.Pais_Nacionalidad')
            registro.pais_origen = request.POST.get('registro.pais_origen')
            registro.uci = request.POST.get('registro.uci')
            registro.municipio_res_id = request.POST.get('registro.municipio_res_id')
            registro.origen = request.POST.get('registro.origen')
            registro.sector = request.POST.get('registro.sector')
            registro.sexo = request.POST.get('registro.sexo')
            registro.tipo_paciente = request.POST.get('registro.tipo_paciente')
            registro.save()
            return redirect('listar')
    else:
        return render(request, "crud_datos/agregar.html")

def actualizar(request):
    if request.method=='POST':
        if request.POST.get('fechaact') and request.POST.get('id') and request.POST.get('EntidadNac') and request.POST.get('EntidadUM') and request.POST.get('entidad_res_id') and request.POST.get('fecha_ingreso') and request.POST.get('fecha_Sintomas') and  request.POST.get('fecha_def') and request.POST.get('intubado') and request.POST.get('neumonia') and request.POST.get('edad') and request.POST.get('nacionalidad') and  request.POST.get('embarazo') and request.POST.get('habla_lengua_indigena') and request.POST.get('diabetes') and request.POST.get('epoc') and request.POST.get('asma') and request.POST.get('inmusupr') and request.POST.get('otra_com') and request.POST.get('cardiovascular') and request.POST.get('obesidad') and request.POST.get('renal cronica') and request.POST.get('tabaquismo') and  request.POST.get('otro_caso') and request.POST.get('resultado') and request.POST.get('migrante') and request.POST.get('Pais_Nacionalidad') and request.POST.get('pais_origen') and request.POST.get('uci') and request.POST.get('municipio_res_id') and request.POST.get('origen') and request.POST.get('sector') and request.POST.get('sexo') and request.POST.get('tipo_paciente'):
            registro = setDatos()
            registro.fechaact = request.POST.get('registro.fechaact')
            registro.idregistro = request.POST.get('registro.id')
            registro.EntidadNac = request.POST.get('registro.EntidadNac')
            registro.EntidadUM = request.POST.get('registro.EntidadUM')
            registro.entidad_res_id = request.POST.get('registro.entidad_res_id')
            registro.fecha_ingreso = request.POST.get('registro.fecha_ingreso')
            registro.fecha_Sintomas = request.POST.get('registro.fecha_Sintomas')
            registro.fecha_def = request.POST.get('registro.fecha_def')
            registro.intubado = request.POST.get('registro.intubado')
            registro.neumonia = request.POST.get('registro.neumonia')
            registro.edad = request.POST.get('registro.edad')
            registro.nacionalidad = request.POST.get('registro.nacionalidad')
            registro.embarazo = request.POST.get('registro.embarazo')
            registro.habla_lengua_indigena = request.POST.get('registro.habla_lengua_indigena')
            registro.diabetes = request.POST.get('registro.diabetes')
            registro.epoc = request.POST.get('registro.epoc')
            registro.asma = request.POST.get('registro.asma')
            registro.inmunosupr = request.POST.get('registro.inmunosupr')
            registro.otra_com = request.POST.get('registro.otra_com')
            registro.cardiovascular = request.POST.get('registro.cardiovascular')
            registro.obesidad = request.POST.get('registro.obesidad')
            registro.renal_cronica = request.POST.get('registro.renal cronica')
            registro.tabaquismo = request.POST.get('registro.tabaquismo')
            registro.otro_caso = request.POST.get('registro.otro_caso')
            registro.resultado = request.POST.get('registro.resultado')
            registro.migrante = request.POST.get('registro.migrante')
            registro.Pais_Nacionalidad = request.POST.get('registro.Pais_Nacionalidad')
            registro.pais_origen = request.POST.get('registro.pais_origen')
            registro.uci = request.POST.get('registro.uci')
            registro.municipio_res_id = request.POST.get('registro.municipio_res_id')
            registro.origen = request.POST.get('registro.origen')
            registro.sector = request.POST.get('registro.sector')
            registro.sexo = request.POST.get('registro.sexo')
            registro.tipo_paciente = request.POST.get('registro.tipo_paciente')
            registro.save()
            return redirect('listar')

    else:
        alldata = setDatos.objects.all()
        datos = {'setDatos' : alldata}
        return render(request, "crud_datos/actualizar.html", datos)

def eliminar(request):
    if request.method=='POST':
        if request.POST.get('id'):
            id_a_borrar = request.POST.get('id')
            tupla = setDatos.objects.get(id=id_a_borrar)
            tupla.delete()
    alldata = setDatos.objects.all()
    datos = {'setDatos' : alldata}
    return render(request, "crud_datos/eliminar.html", datos)

def home(request):
    # Obtener los parámetros de fecha seleccionados por el usuario
    fecha_inicio = request.GET.get('fecha_inicio', '2020-01-01')
    fecha_fin = request.GET.get('fecha_fin', '2022-12-31')

    # Convertir las fechas en objetos Date
    fecha_inicio = date.fromisoformat(fecha_inicio)
    fecha_fin = date.fromisoformat(fecha_fin)

    # Filtrar los datos de COVID-19 en el rango de fechas seleccionado
    datos_filtrados = setDatos.objects.filter(
        FECHA_ACTUALIZACION__gte=fecha_inicio,
        FECHA_ACTUALIZACION__lte=fecha_fin
    )

    # Procesar los datos para contar los casos por entidad
    casos_por_entidad = {}
    for dato in datos_filtrados:
        entidad = dato.ENTIDAD_UM  # Reemplaza esto con el nombre real de la columna
        if entidad in casos_por_entidad:
            casos_por_entidad[entidad] += 1
        else:
            casos_por_entidad[entidad] = 1

    # Preparar los datos para el gráfico de barras
    labels = list(casos_por_entidad.keys())
    data = list(casos_por_entidad.values())

    labels2 = {
        'labels': labels,
    }
    data2 = {
        'data': data,
    }

    return render(request, 'crud_datos/home.html', labels2,data2)