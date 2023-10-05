# Generated by Django 4.2.5 on 2023-10-05 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidIA', '0005_alter_setdatos_asma_alter_setdatos_cardiovascular_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setdatos',
            name='ASMA',
            field=models.CharField(choices=[('99', 'no especificado'), ('1', 'si'), ('2', 'no'), ('98', 'se ignora'), ('97', 'no aplica')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='CARDIOVASCULAR',
            field=models.CharField(choices=[('99', 'no especificado'), ('1', 'si'), ('2', 'no'), ('98', 'se ignora'), ('97', 'no aplica')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='DIABETES',
            field=models.CharField(choices=[('99', 'no especificado'), ('1', 'si'), ('2', 'no'), ('98', 'se ignora'), ('97', 'no aplica')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='EMBARAZO',
            field=models.CharField(choices=[('99', 'no especificado'), ('1', 'si'), ('2', 'no'), ('98', 'se ignora'), ('97', 'no aplica')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='ENTIDAD_NAC',
            field=models.CharField(choices=[('7', 'CHIAPAS'), ('17', 'MORELOS'), ('12', 'GUERRERO'), ('30', 'VERACRUZ DE IGNACIO DE LA LLAVE'), ('31', 'YUCATÁN'), ('97', 'NO APLICA'), ('28', 'TAMAULIPAS'), ('16', 'MICHOACÁN DE OCAMPO'), ('98', 'SE IGNORA'), ('6', 'COLIMA'), ('20', 'OAXACA'), ('24', 'SAN LUIS POTOSÍ'), ('22', 'QUERÉTARO'), ('25', 'SINALOA'), ('3', 'BAJA CALIFORNIA SUR'), ('26', 'SONORA'), ('11', 'GUANAJUATO'), ('15', 'MÉXICO'), ('29', 'TLAXCALA'), ('10', 'DURANGO'), ('2', 'BAJA CALIFORNIA'), ('27', 'TABASCO'), ('4', 'CAMPECHE'), ('9', 'CIUDAD DE MÉXICO'), ('32', 'ZACATECAS'), ('5', 'COAHUILA DE ZARAGOZA'), ('19', 'NUEVO LEÓN'), ('21', 'PUEBLA'), ('36', 'ESTADOS UNIDOS MEXICANOS'), ('99', 'NO ESPECIFICADO'), ('13', 'HIDALGO'), ('1', 'AGUASCALIENTES'), ('18', 'NAYARIT'), ('14', 'JALISCO'), ('8', 'CHIHUAHUA'), ('23', 'QUINTANA ROO')], default='99', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='ENTIDAD_UM',
            field=models.CharField(choices=[('7', 'CHIAPAS'), ('17', 'MORELOS'), ('12', 'GUERRERO'), ('30', 'VERACRUZ DE IGNACIO DE LA LLAVE'), ('31', 'YUCATÁN'), ('97', 'NO APLICA'), ('28', 'TAMAULIPAS'), ('16', 'MICHOACÁN DE OCAMPO'), ('98', 'SE IGNORA'), ('6', 'COLIMA'), ('20', 'OAXACA'), ('24', 'SAN LUIS POTOSÍ'), ('22', 'QUERÉTARO'), ('25', 'SINALOA'), ('3', 'BAJA CALIFORNIA SUR'), ('26', 'SONORA'), ('11', 'GUANAJUATO'), ('15', 'MÉXICO'), ('29', 'TLAXCALA'), ('10', 'DURANGO'), ('2', 'BAJA CALIFORNIA'), ('27', 'TABASCO'), ('4', 'CAMPECHE'), ('9', 'CIUDAD DE MÉXICO'), ('32', 'ZACATECAS'), ('5', 'COAHUILA DE ZARAGOZA'), ('19', 'NUEVO LEÓN'), ('21', 'PUEBLA'), ('36', 'ESTADOS UNIDOS MEXICANOS'), ('99', 'NO ESPECIFICADO'), ('13', 'HIDALGO'), ('1', 'AGUASCALIENTES'), ('18', 'NAYARIT'), ('14', 'JALISCO'), ('8', 'CHIHUAHUA'), ('23', 'QUINTANA ROO')], default='99', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='EPOC',
            field=models.CharField(choices=[('99', 'no especificado'), ('1', 'si'), ('2', 'no'), ('98', 'se ignora'), ('97', 'no aplica')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='HABLA_LENGUA_INDIG',
            field=models.CharField(choices=[('99', 'no especificado'), ('1', 'si'), ('2', 'no'), ('98', 'se ignora'), ('97', 'no aplica')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='HIPERTENSION',
            field=models.CharField(choices=[('99', 'no especificado'), ('1', 'si'), ('2', 'no'), ('98', 'se ignora'), ('97', 'no aplica')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='INMUSUPR',
            field=models.CharField(choices=[('99', 'no especificado'), ('1', 'si'), ('2', 'no'), ('98', 'se ignora'), ('97', 'no aplica')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='INTUBADO',
            field=models.CharField(choices=[('99', 'no especificado'), ('1', 'si'), ('2', 'no'), ('98', 'se ignora'), ('97', 'no aplica')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='MIGRANTE',
            field=models.CharField(choices=[('99', 'no especificado'), ('1', 'si'), ('2', 'no'), ('98', 'se ignora'), ('97', 'no aplica')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='NEUMONIA',
            field=models.CharField(choices=[('99', 'no especificado'), ('1', 'si'), ('2', 'no'), ('98', 'se ignora'), ('97', 'no aplica')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='OBESIDAD',
            field=models.CharField(choices=[('99', 'no especificado'), ('1', 'si'), ('2', 'no'), ('98', 'se ignora'), ('97', 'no aplica')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='ORIGEN',
            field=models.CharField(choices=[('1', 'USMER'), ('2', 'FUERA DE USMER'), ('99', 'NO ESPECIFICADO')], default='99', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='OTRA_COM',
            field=models.CharField(choices=[('99', 'no especificado'), ('1', 'si'), ('2', 'no'), ('98', 'se ignora'), ('97', 'no aplica')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='OTRO_CASO',
            field=models.CharField(choices=[('99', 'no especificado'), ('1', 'si'), ('2', 'no'), ('98', 'se ignora'), ('97', 'no aplica')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='RENAL_CRONICA',
            field=models.CharField(choices=[('99', 'no especificado'), ('1', 'si'), ('2', 'no'), ('98', 'se ignora'), ('97', 'no aplica')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='RESULTADO',
            field=models.CharField(choices=[('1', 'positivo SARS-CoV-2'), ('2', 'no positivo SARS-CoV-2'), ('99', 'resultado pendiente')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='SECTOR',
            field=models.CharField(choices=[('3', 'ESTATAL'), ('10', 'SEDENA'), ('13', 'UNIVERSITARIO'), ('4', 'IMSS'), ('8', 'PEMEX'), ('1', 'CRUZ ROJA'), ('9', 'PRIVADA'), ('99', 'NO ESPECIFICADO'), ('7', 'MUNICIPAL'), ('12', 'SSA'), ('6', 'ISSSTE'), ('2', 'DIF'), ('5', 'IMSS-BIENESTAR'), ('11', 'SEMAR')], default='99', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='SEXO',
            field=models.CharField(choices=[('1', 'mujer'), ('99', 'NO ESPECIFICADO'), ('2', 'hombre')], default='99', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='TABAQUISMO',
            field=models.CharField(choices=[('99', 'no especificado'), ('1', 'si'), ('2', 'no'), ('98', 'se ignora'), ('97', 'no aplica')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='TIPO_PACIENTE',
            field=models.CharField(choices=[('2', 'HOSPITALZADO'), ('1', 'AMBULATORIA'), ('99', 'NO ESPECIFICADO')], default='99', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='UCI',
            field=models.CharField(choices=[('99', 'no especificado'), ('1', 'si'), ('2', 'no'), ('98', 'se ignora'), ('97', 'no aplica')], default='1', max_length=2),
        ),
    ]
