# Generated by Django 4.2.5 on 2023-10-04 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidIA', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setdatos',
            name='ASMA',
            field=models.CharField(choices=[('2', 'no'), ('98', 'se ignora'), ('97', 'no aplica'), ('1', 'si'), ('99', 'no especificado')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='CARDIOVASCULAR',
            field=models.CharField(choices=[('2', 'no'), ('98', 'se ignora'), ('97', 'no aplica'), ('1', 'si'), ('99', 'no especificado')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='DIABETES',
            field=models.CharField(choices=[('2', 'no'), ('98', 'se ignora'), ('97', 'no aplica'), ('1', 'si'), ('99', 'no especificado')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='EMBARAZO',
            field=models.CharField(choices=[('2', 'no'), ('98', 'se ignora'), ('97', 'no aplica'), ('1', 'si'), ('99', 'no especificado')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='ENTIDAD_NAC',
            field=models.CharField(choices=[('16', 'MICHOACÁN DE OCAMPO'), ('25', 'SINALOA'), ('09', 'CIUDAD DE MÉXICO'), ('21', 'PUEBLA'), ('03', 'BAJA CALIFORNIA SUR'), ('98', 'SE IGNORA'), ('04', 'CAMPECHE'), ('07', 'CHIAPAS'), ('31', 'YUCATÁN'), ('36', 'ESTADOS UNIDOS MEXICANOS'), ('01', 'AGUASCALIENTES'), ('12', 'GUERRERO'), ('08', 'CHIHUAHUA'), ('18', 'NAYARIT'), ('22', 'QUERÉTARO'), ('14', 'JALISCO'), ('30', 'VERACRUZ DE IGNACIO DE LA LLAVE'), ('27', 'TABASCO'), ('28', 'TAMAULIPAS'), ('19', 'NUEVO LEÓN'), ('10', 'DURANGO'), ('05', 'COAHUILA DE ZARAGOZA'), ('99', 'NO ESPECIFICADO'), ('24', 'SAN LUIS POTOSÍ'), ('32', 'ZACATECAS'), ('97', 'NO APLICA'), ('29', 'TLAXCALA'), ('13', 'HIDALGO'), ('06', 'COLIMA'), ('26', 'SONORA'), ('17', 'MORELOS'), ('11', 'GUANAJUATO'), ('20', 'OAXACA'), ('23', 'QUINTANA ROO'), ('15', 'MÉXICO'), ('02', 'BAJA CALIFORNIA')], default='99', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='ENTIDAD_RES',
            field=models.CharField(choices=[('16', 'MICHOACÁN DE OCAMPO'), ('25', 'SINALOA'), ('09', 'CIUDAD DE MÉXICO'), ('21', 'PUEBLA'), ('03', 'BAJA CALIFORNIA SUR'), ('98', 'SE IGNORA'), ('04', 'CAMPECHE'), ('07', 'CHIAPAS'), ('31', 'YUCATÁN'), ('36', 'ESTADOS UNIDOS MEXICANOS'), ('01', 'AGUASCALIENTES'), ('12', 'GUERRERO'), ('08', 'CHIHUAHUA'), ('18', 'NAYARIT'), ('22', 'QUERÉTARO'), ('14', 'JALISCO'), ('30', 'VERACRUZ DE IGNACIO DE LA LLAVE'), ('27', 'TABASCO'), ('28', 'TAMAULIPAS'), ('19', 'NUEVO LEÓN'), ('10', 'DURANGO'), ('05', 'COAHUILA DE ZARAGOZA'), ('99', 'NO ESPECIFICADO'), ('24', 'SAN LUIS POTOSÍ'), ('32', 'ZACATECAS'), ('97', 'NO APLICA'), ('29', 'TLAXCALA'), ('13', 'HIDALGO'), ('06', 'COLIMA'), ('26', 'SONORA'), ('17', 'MORELOS'), ('11', 'GUANAJUATO'), ('20', 'OAXACA'), ('23', 'QUINTANA ROO'), ('15', 'MÉXICO'), ('02', 'BAJA CALIFORNIA')], default='99', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='ENTIDAD_UM',
            field=models.CharField(choices=[('16', 'MICHOACÁN DE OCAMPO'), ('25', 'SINALOA'), ('09', 'CIUDAD DE MÉXICO'), ('21', 'PUEBLA'), ('03', 'BAJA CALIFORNIA SUR'), ('98', 'SE IGNORA'), ('04', 'CAMPECHE'), ('07', 'CHIAPAS'), ('31', 'YUCATÁN'), ('36', 'ESTADOS UNIDOS MEXICANOS'), ('01', 'AGUASCALIENTES'), ('12', 'GUERRERO'), ('08', 'CHIHUAHUA'), ('18', 'NAYARIT'), ('22', 'QUERÉTARO'), ('14', 'JALISCO'), ('30', 'VERACRUZ DE IGNACIO DE LA LLAVE'), ('27', 'TABASCO'), ('28', 'TAMAULIPAS'), ('19', 'NUEVO LEÓN'), ('10', 'DURANGO'), ('05', 'COAHUILA DE ZARAGOZA'), ('99', 'NO ESPECIFICADO'), ('24', 'SAN LUIS POTOSÍ'), ('32', 'ZACATECAS'), ('97', 'NO APLICA'), ('29', 'TLAXCALA'), ('13', 'HIDALGO'), ('06', 'COLIMA'), ('26', 'SONORA'), ('17', 'MORELOS'), ('11', 'GUANAJUATO'), ('20', 'OAXACA'), ('23', 'QUINTANA ROO'), ('15', 'MÉXICO'), ('02', 'BAJA CALIFORNIA')], default='99', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='EPOC',
            field=models.CharField(choices=[('2', 'no'), ('98', 'se ignora'), ('97', 'no aplica'), ('1', 'si'), ('99', 'no especificado')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='HABLA_LENGUA_INDIG',
            field=models.CharField(choices=[('2', 'no'), ('98', 'se ignora'), ('97', 'no aplica'), ('1', 'si'), ('99', 'no especificado')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='HIPERTENSION',
            field=models.CharField(choices=[('2', 'no'), ('98', 'se ignora'), ('97', 'no aplica'), ('1', 'si'), ('99', 'no especificado')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='INMUSUPR',
            field=models.CharField(choices=[('2', 'no'), ('98', 'se ignora'), ('97', 'no aplica'), ('1', 'si'), ('99', 'no especificado')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='INTUBADO',
            field=models.CharField(choices=[('2', 'no'), ('98', 'se ignora'), ('97', 'no aplica'), ('1', 'si'), ('99', 'no especificado')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='MIGRANTE',
            field=models.CharField(choices=[('2', 'no'), ('98', 'se ignora'), ('97', 'no aplica'), ('1', 'si'), ('99', 'no especificado')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='NACIONALIDAD',
            field=models.CharField(choices=[('2', 'extranjera'), ('1', 'mexicana'), ('99', 'no especificado')], default='99', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='NEUMONIA',
            field=models.CharField(choices=[('2', 'no'), ('98', 'se ignora'), ('97', 'no aplica'), ('1', 'si'), ('99', 'no especificado')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='OBESIDAD',
            field=models.CharField(choices=[('2', 'no'), ('98', 'se ignora'), ('97', 'no aplica'), ('1', 'si'), ('99', 'no especificado')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='OTRA_COM',
            field=models.CharField(choices=[('2', 'no'), ('98', 'se ignora'), ('97', 'no aplica'), ('1', 'si'), ('99', 'no especificado')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='OTRO_CASO',
            field=models.CharField(choices=[('2', 'no'), ('98', 'se ignora'), ('97', 'no aplica'), ('1', 'si'), ('99', 'no especificado')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='PAIS_NACIONALIDAD',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='PAIS_ORIGEN',
            field=models.CharField(choices=[('2', 'extranjera'), ('1', 'mexicana'), ('99', 'no especificado')], default='99', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='RENAL_CRONICA',
            field=models.CharField(choices=[('2', 'no'), ('98', 'se ignora'), ('97', 'no aplica'), ('1', 'si'), ('99', 'no especificado')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='RESULTADO',
            field=models.CharField(choices=[('2', 'no'), ('98', 'se ignora'), ('97', 'no aplica'), ('1', 'si'), ('99', 'no especificado')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='TABAQUISMO',
            field=models.CharField(choices=[('2', 'no'), ('98', 'se ignora'), ('97', 'no aplica'), ('1', 'si'), ('99', 'no especificado')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='UCI',
            field=models.CharField(choices=[('2', 'no'), ('98', 'se ignora'), ('97', 'no aplica'), ('1', 'si'), ('99', 'no especificado')], default='1', max_length=2),
        ),
    ]
