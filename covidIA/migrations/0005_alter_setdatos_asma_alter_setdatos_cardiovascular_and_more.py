# Generated by Django 4.2.5 on 2023-10-04 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidIA', '0004_alter_municipios_clave_alter_setdatos_asma_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setdatos',
            name='ASMA',
            field=models.CharField(choices=[('1', 'si'), ('99', 'no especificado'), ('2', 'no'), ('97', 'no aplica'), ('98', 'se ignora')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='CARDIOVASCULAR',
            field=models.CharField(choices=[('1', 'si'), ('99', 'no especificado'), ('2', 'no'), ('97', 'no aplica'), ('98', 'se ignora')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='DIABETES',
            field=models.CharField(choices=[('1', 'si'), ('99', 'no especificado'), ('2', 'no'), ('97', 'no aplica'), ('98', 'se ignora')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='EMBARAZO',
            field=models.CharField(choices=[('1', 'si'), ('99', 'no especificado'), ('2', 'no'), ('97', 'no aplica'), ('98', 'se ignora')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='ENTIDAD_NAC',
            field=models.CharField(choices=[('06', 'COLIMA'), ('14', 'JALISCO'), ('04', 'CAMPECHE'), ('19', 'NUEVO LEÓN'), ('08', 'CHIHUAHUA'), ('23', 'QUINTANA ROO'), ('21', 'PUEBLA'), ('05', 'COAHUILA DE ZARAGOZA'), ('20', 'OAXACA'), ('99', 'NO ESPECIFICADO'), ('03', 'BAJA CALIFORNIA SUR'), ('28', 'TAMAULIPAS'), ('02', 'BAJA CALIFORNIA'), ('27', 'TABASCO'), ('30', 'VERACRUZ DE IGNACIO DE LA LLAVE'), ('98', 'SE IGNORA'), ('17', 'MORELOS'), ('13', 'HIDALGO'), ('25', 'SINALOA'), ('97', 'NO APLICA'), ('29', 'TLAXCALA'), ('07', 'CHIAPAS'), ('26', 'SONORA'), ('31', 'YUCATÁN'), ('09', 'CIUDAD DE MÉXICO'), ('16', 'MICHOACÁN DE OCAMPO'), ('36', 'ESTADOS UNIDOS MEXICANOS'), ('18', 'NAYARIT'), ('24', 'SAN LUIS POTOSÍ'), ('15', 'MÉXICO'), ('22', 'QUERÉTARO'), ('01', 'AGUASCALIENTES'), ('10', 'DURANGO'), ('12', 'GUERRERO'), ('32', 'ZACATECAS'), ('11', 'GUANAJUATO')], default='99', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='ENTIDAD_UM',
            field=models.CharField(choices=[('06', 'COLIMA'), ('14', 'JALISCO'), ('04', 'CAMPECHE'), ('19', 'NUEVO LEÓN'), ('08', 'CHIHUAHUA'), ('23', 'QUINTANA ROO'), ('21', 'PUEBLA'), ('05', 'COAHUILA DE ZARAGOZA'), ('20', 'OAXACA'), ('99', 'NO ESPECIFICADO'), ('03', 'BAJA CALIFORNIA SUR'), ('28', 'TAMAULIPAS'), ('02', 'BAJA CALIFORNIA'), ('27', 'TABASCO'), ('30', 'VERACRUZ DE IGNACIO DE LA LLAVE'), ('98', 'SE IGNORA'), ('17', 'MORELOS'), ('13', 'HIDALGO'), ('25', 'SINALOA'), ('97', 'NO APLICA'), ('29', 'TLAXCALA'), ('07', 'CHIAPAS'), ('26', 'SONORA'), ('31', 'YUCATÁN'), ('09', 'CIUDAD DE MÉXICO'), ('16', 'MICHOACÁN DE OCAMPO'), ('36', 'ESTADOS UNIDOS MEXICANOS'), ('18', 'NAYARIT'), ('24', 'SAN LUIS POTOSÍ'), ('15', 'MÉXICO'), ('22', 'QUERÉTARO'), ('01', 'AGUASCALIENTES'), ('10', 'DURANGO'), ('12', 'GUERRERO'), ('32', 'ZACATECAS'), ('11', 'GUANAJUATO')], default='99', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='EPOC',
            field=models.CharField(choices=[('1', 'si'), ('99', 'no especificado'), ('2', 'no'), ('97', 'no aplica'), ('98', 'se ignora')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='HABLA_LENGUA_INDIG',
            field=models.CharField(choices=[('1', 'si'), ('99', 'no especificado'), ('2', 'no'), ('97', 'no aplica'), ('98', 'se ignora')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='HIPERTENSION',
            field=models.CharField(choices=[('1', 'si'), ('99', 'no especificado'), ('2', 'no'), ('97', 'no aplica'), ('98', 'se ignora')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='INMUSUPR',
            field=models.CharField(choices=[('1', 'si'), ('99', 'no especificado'), ('2', 'no'), ('97', 'no aplica'), ('98', 'se ignora')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='INTUBADO',
            field=models.CharField(choices=[('1', 'si'), ('99', 'no especificado'), ('2', 'no'), ('97', 'no aplica'), ('98', 'se ignora')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='MIGRANTE',
            field=models.CharField(choices=[('1', 'si'), ('99', 'no especificado'), ('2', 'no'), ('97', 'no aplica'), ('98', 'se ignora')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='NEUMONIA',
            field=models.CharField(choices=[('1', 'si'), ('99', 'no especificado'), ('2', 'no'), ('97', 'no aplica'), ('98', 'se ignora')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='OBESIDAD',
            field=models.CharField(choices=[('1', 'si'), ('99', 'no especificado'), ('2', 'no'), ('97', 'no aplica'), ('98', 'se ignora')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='ORIGEN',
            field=models.CharField(choices=[('99', 'NO ESPECIFICADO'), ('1', 'USMER'), ('2', 'FUERA DE USMER')], default='99', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='OTRA_COM',
            field=models.CharField(choices=[('1', 'si'), ('99', 'no especificado'), ('2', 'no'), ('97', 'no aplica'), ('98', 'se ignora')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='OTRO_CASO',
            field=models.CharField(choices=[('1', 'si'), ('99', 'no especificado'), ('2', 'no'), ('97', 'no aplica'), ('98', 'se ignora')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='RENAL_CRONICA',
            field=models.CharField(choices=[('1', 'si'), ('99', 'no especificado'), ('2', 'no'), ('97', 'no aplica'), ('98', 'se ignora')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='RESULTADO',
            field=models.CharField(choices=[('1', 'positivo SARS-CoV-2'), ('99', 'resultado pendiente'), ('2', 'no positivo SARS-CoV-2')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='SECTOR',
            field=models.CharField(choices=[('2', 'DIF'), ('1', 'CRUZ ROJA'), ('7', 'MUNICIPAL'), ('6', 'ISSSTE'), ('11', 'SEMAR'), ('4', 'IMSS'), ('8', 'PEMEX'), ('10', 'SEDENA'), ('3', 'ESTATAL'), ('5', 'IMSS-BIENESTAR'), ('13', 'UNIVERSITARIO'), ('99', 'NO ESPECIFICADO'), ('9', 'PRIVADA'), ('12', 'SSA')], default='99', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='SEXO',
            field=models.CharField(choices=[('99', 'NO ESPECIFICADO'), ('1', 'mujer'), ('2', 'hombre')], default='99', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='TABAQUISMO',
            field=models.CharField(choices=[('1', 'si'), ('99', 'no especificado'), ('2', 'no'), ('97', 'no aplica'), ('98', 'se ignora')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='TIPO_PACIENTE',
            field=models.CharField(choices=[('99', 'NO ESPECIFICADO'), ('1', 'AMBULATORIA'), ('2', 'HOSPITALZADO')], default='99', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='UCI',
            field=models.CharField(choices=[('1', 'si'), ('99', 'no especificado'), ('2', 'no'), ('97', 'no aplica'), ('98', 'se ignora')], default='1', max_length=2),
        ),
    ]