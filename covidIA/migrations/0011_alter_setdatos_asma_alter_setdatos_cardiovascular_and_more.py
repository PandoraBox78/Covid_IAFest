# Generated by Django 4.2.5 on 2023-10-05 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('covidIA', '0010_alter_setdatos_asma_alter_setdatos_cardiovascular_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setdatos',
            name='ASMA',
            field=models.CharField(choices=[('99', 'no especificado'), ('2', 'no'), ('97', 'no aplica'), ('98', 'se ignora'), ('1', 'si')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='CARDIOVASCULAR',
            field=models.CharField(choices=[('99', 'no especificado'), ('2', 'no'), ('97', 'no aplica'), ('98', 'se ignora'), ('1', 'si')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='DIABETES',
            field=models.CharField(choices=[('99', 'no especificado'), ('2', 'no'), ('97', 'no aplica'), ('98', 'se ignora'), ('1', 'si')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='EMBARAZO',
            field=models.CharField(choices=[('99', 'no especificado'), ('2', 'no'), ('97', 'no aplica'), ('98', 'se ignora'), ('1', 'si')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='ENTIDAD_NAC',
            field=models.CharField(choices=[('4', 'CAMPECHE'), ('20', 'OAXACA'), ('28', 'TAMAULIPAS'), ('8', 'CHIHUAHUA'), ('13', 'HIDALGO'), ('9', 'CIUDAD DE MÉXICO'), ('17', 'MORELOS'), ('6', 'COLIMA'), ('14', 'JALISCO'), ('21', 'PUEBLA'), ('97', 'NO APLICA'), ('3', 'BAJA CALIFORNIA SUR'), ('24', 'SAN LUIS POTOSÍ'), ('30', 'VERACRUZ DE IGNACIO DE LA LLAVE'), ('32', 'ZACATECAS'), ('31', 'YUCATÁN'), ('2', 'BAJA CALIFORNIA'), ('18', 'NAYARIT'), ('10', 'DURANGO'), ('1', 'AGUASCALIENTES'), ('19', 'NUEVO LEÓN'), ('98', 'SE IGNORA'), ('36', 'ESTADOS UNIDOS MEXICANOS'), ('25', 'SINALOA'), ('27', 'TABASCO'), ('26', 'SONORA'), ('7', 'CHIAPAS'), ('5', 'COAHUILA DE ZARAGOZA'), ('16', 'MICHOACÁN DE OCAMPO'), ('99', 'NO ESPECIFICADO'), ('12', 'GUERRERO'), ('11', 'GUANAJUATO'), ('15', 'MÉXICO'), ('22', 'QUERÉTARO'), ('29', 'TLAXCALA'), ('23', 'QUINTANA ROO')], default='99', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='ENTIDAD_RES',
            field=models.ForeignKey(default='99', null=True, on_delete=django.db.models.deletion.CASCADE, to='covidIA.estados'),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='ENTIDAD_UM',
            field=models.CharField(choices=[('4', 'CAMPECHE'), ('20', 'OAXACA'), ('28', 'TAMAULIPAS'), ('8', 'CHIHUAHUA'), ('13', 'HIDALGO'), ('9', 'CIUDAD DE MÉXICO'), ('17', 'MORELOS'), ('6', 'COLIMA'), ('14', 'JALISCO'), ('21', 'PUEBLA'), ('97', 'NO APLICA'), ('3', 'BAJA CALIFORNIA SUR'), ('24', 'SAN LUIS POTOSÍ'), ('30', 'VERACRUZ DE IGNACIO DE LA LLAVE'), ('32', 'ZACATECAS'), ('31', 'YUCATÁN'), ('2', 'BAJA CALIFORNIA'), ('18', 'NAYARIT'), ('10', 'DURANGO'), ('1', 'AGUASCALIENTES'), ('19', 'NUEVO LEÓN'), ('98', 'SE IGNORA'), ('36', 'ESTADOS UNIDOS MEXICANOS'), ('25', 'SINALOA'), ('27', 'TABASCO'), ('26', 'SONORA'), ('7', 'CHIAPAS'), ('5', 'COAHUILA DE ZARAGOZA'), ('16', 'MICHOACÁN DE OCAMPO'), ('99', 'NO ESPECIFICADO'), ('12', 'GUERRERO'), ('11', 'GUANAJUATO'), ('15', 'MÉXICO'), ('22', 'QUERÉTARO'), ('29', 'TLAXCALA'), ('23', 'QUINTANA ROO')], default='99', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='EPOC',
            field=models.CharField(choices=[('99', 'no especificado'), ('2', 'no'), ('97', 'no aplica'), ('98', 'se ignora'), ('1', 'si')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='FECHA_ACTUALIZACION',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='HABLA_LENGUA_INDIG',
            field=models.CharField(choices=[('99', 'no especificado'), ('2', 'no'), ('97', 'no aplica'), ('98', 'se ignora'), ('1', 'si')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='HIPERTENSION',
            field=models.CharField(choices=[('99', 'no especificado'), ('2', 'no'), ('97', 'no aplica'), ('98', 'se ignora'), ('1', 'si')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='INMUSUPR',
            field=models.CharField(choices=[('99', 'no especificado'), ('2', 'no'), ('97', 'no aplica'), ('98', 'se ignora'), ('1', 'si')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='INTUBADO',
            field=models.CharField(choices=[('99', 'no especificado'), ('2', 'no'), ('97', 'no aplica'), ('98', 'se ignora'), ('1', 'si')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='MIGRANTE',
            field=models.CharField(choices=[('99', 'no especificado'), ('2', 'no'), ('97', 'no aplica'), ('98', 'se ignora'), ('1', 'si')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='MUNICIPIO_RES',
            field=models.ForeignKey(default='99', null=True, on_delete=django.db.models.deletion.CASCADE, to='covidIA.municipios'),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='NACIONALIDAD',
            field=models.CharField(choices=[('2', 'extranjera'), ('1', 'mexicana'), ('99', 'no especificado')], default='99', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='NEUMONIA',
            field=models.CharField(choices=[('99', 'no especificado'), ('2', 'no'), ('97', 'no aplica'), ('98', 'se ignora'), ('1', 'si')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='OBESIDAD',
            field=models.CharField(choices=[('99', 'no especificado'), ('2', 'no'), ('97', 'no aplica'), ('98', 'se ignora'), ('1', 'si')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='OTRA_COM',
            field=models.CharField(choices=[('99', 'no especificado'), ('2', 'no'), ('97', 'no aplica'), ('98', 'se ignora'), ('1', 'si')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='OTRO_CASO',
            field=models.CharField(choices=[('99', 'no especificado'), ('2', 'no'), ('97', 'no aplica'), ('98', 'se ignora'), ('1', 'si')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='PAIS_ORIGEN',
            field=models.CharField(choices=[('2', 'extranjera'), ('1', 'mexicana'), ('99', 'no especificado')], default='99', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='RENAL_CRONICA',
            field=models.CharField(choices=[('99', 'no especificado'), ('2', 'no'), ('97', 'no aplica'), ('98', 'se ignora'), ('1', 'si')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='SECTOR',
            field=models.CharField(choices=[('6', 'ISSSTE'), ('99', 'NO ESPECIFICADO'), ('3', 'ESTATAL'), ('2', 'DIF'), ('1', 'CRUZ ROJA'), ('7', 'MUNICIPAL'), ('13', 'UNIVERSITARIO'), ('5', 'IMSS-BIENESTAR'), ('4', 'IMSS'), ('11', 'SEMAR'), ('10', 'SEDENA'), ('8', 'PEMEX'), ('12', 'SSA'), ('9', 'PRIVADA')], default='99', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='SEXO',
            field=models.CharField(choices=[('1', 'mujer'), ('2', 'hombre'), ('99', 'NO ESPECIFICADO')], default='99', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='TABAQUISMO',
            field=models.CharField(choices=[('99', 'no especificado'), ('2', 'no'), ('97', 'no aplica'), ('98', 'se ignora'), ('1', 'si')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='TIPO_PACIENTE',
            field=models.CharField(choices=[('1', 'AMBULATORIA'), ('2', 'HOSPITALZADO'), ('99', 'NO ESPECIFICADO')], default='99', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='UCI',
            field=models.CharField(choices=[('99', 'no especificado'), ('2', 'no'), ('97', 'no aplica'), ('98', 'se ignora'), ('1', 'si')], default='1', max_length=2),
        ),
    ]