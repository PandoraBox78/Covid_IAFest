# Generated by Django 4.2.5 on 2023-10-05 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('covidIA', '0009_alter_setdatos_asma_alter_setdatos_cardiovascular_and_more'),
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
            field=models.CharField(choices=[('7', 'CHIAPAS'), ('25', 'SINALOA'), ('98', 'SE IGNORA'), ('19', 'NUEVO LEÓN'), ('28', 'TAMAULIPAS'), ('16', 'MICHOACÁN DE OCAMPO'), ('20', 'OAXACA'), ('97', 'NO APLICA'), ('99', 'NO ESPECIFICADO'), ('9', 'CIUDAD DE MÉXICO'), ('30', 'VERACRUZ DE IGNACIO DE LA LLAVE'), ('14', 'JALISCO'), ('1', 'AGUASCALIENTES'), ('23', 'QUINTANA ROO'), ('12', 'GUERRERO'), ('17', 'MORELOS'), ('5', 'COAHUILA DE ZARAGOZA'), ('15', 'MÉXICO'), ('6', 'COLIMA'), ('22', 'QUERÉTARO'), ('13', 'HIDALGO'), ('3', 'BAJA CALIFORNIA SUR'), ('24', 'SAN LUIS POTOSÍ'), ('18', 'NAYARIT'), ('26', 'SONORA'), ('29', 'TLAXCALA'), ('2', 'BAJA CALIFORNIA'), ('8', 'CHIHUAHUA'), ('11', 'GUANAJUATO'), ('10', 'DURANGO'), ('4', 'CAMPECHE'), ('31', 'YUCATÁN'), ('27', 'TABASCO'), ('36', 'ESTADOS UNIDOS MEXICANOS'), ('32', 'ZACATECAS'), ('21', 'PUEBLA')], default='99', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='ENTIDAD_RES',
            field=models.ForeignKey(default='99', on_delete=django.db.models.deletion.CASCADE, to='covidIA.estados'),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='ENTIDAD_UM',
            field=models.CharField(choices=[('7', 'CHIAPAS'), ('25', 'SINALOA'), ('98', 'SE IGNORA'), ('19', 'NUEVO LEÓN'), ('28', 'TAMAULIPAS'), ('16', 'MICHOACÁN DE OCAMPO'), ('20', 'OAXACA'), ('97', 'NO APLICA'), ('99', 'NO ESPECIFICADO'), ('9', 'CIUDAD DE MÉXICO'), ('30', 'VERACRUZ DE IGNACIO DE LA LLAVE'), ('14', 'JALISCO'), ('1', 'AGUASCALIENTES'), ('23', 'QUINTANA ROO'), ('12', 'GUERRERO'), ('17', 'MORELOS'), ('5', 'COAHUILA DE ZARAGOZA'), ('15', 'MÉXICO'), ('6', 'COLIMA'), ('22', 'QUERÉTARO'), ('13', 'HIDALGO'), ('3', 'BAJA CALIFORNIA SUR'), ('24', 'SAN LUIS POTOSÍ'), ('18', 'NAYARIT'), ('26', 'SONORA'), ('29', 'TLAXCALA'), ('2', 'BAJA CALIFORNIA'), ('8', 'CHIHUAHUA'), ('11', 'GUANAJUATO'), ('10', 'DURANGO'), ('4', 'CAMPECHE'), ('31', 'YUCATÁN'), ('27', 'TABASCO'), ('36', 'ESTADOS UNIDOS MEXICANOS'), ('32', 'ZACATECAS'), ('21', 'PUEBLA')], default='99', max_length=2),
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
            name='MUNICIPIO_RES',
            field=models.ForeignKey(default='99', on_delete=django.db.models.deletion.CASCADE, to='covidIA.municipios'),
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
            name='ORIGEN',
            field=models.CharField(choices=[('99', 'NO ESPECIFICADO'), ('2', 'FUERA DE USMER'), ('1', 'USMER')], default='99', max_length=2),
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
            name='RENAL_CRONICA',
            field=models.CharField(choices=[('2', 'no'), ('98', 'se ignora'), ('97', 'no aplica'), ('1', 'si'), ('99', 'no especificado')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='RESULTADO',
            field=models.CharField(choices=[('1', 'positivo SARS-CoV-2'), ('99', 'resultado pendiente'), ('2', 'no positivo SARS-CoV-2')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='SECTOR',
            field=models.CharField(choices=[('1', 'CRUZ ROJA'), ('99', 'NO ESPECIFICADO'), ('7', 'MUNICIPAL'), ('8', 'PEMEX'), ('6', 'ISSSTE'), ('11', 'SEMAR'), ('12', 'SSA'), ('4', 'IMSS'), ('10', 'SEDENA'), ('9', 'PRIVADA'), ('3', 'ESTATAL'), ('13', 'UNIVERSITARIO'), ('2', 'DIF'), ('5', 'IMSS-BIENESTAR')], default='99', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='SEXO',
            field=models.CharField(choices=[('99', 'NO ESPECIFICADO'), ('2', 'hombre'), ('1', 'mujer')], default='99', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='TABAQUISMO',
            field=models.CharField(choices=[('2', 'no'), ('98', 'se ignora'), ('97', 'no aplica'), ('1', 'si'), ('99', 'no especificado')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='TIPO_PACIENTE',
            field=models.CharField(choices=[('99', 'NO ESPECIFICADO'), ('1', 'AMBULATORIA'), ('2', 'HOSPITALZADO')], default='99', max_length=2),
        ),
        migrations.AlterField(
            model_name='setdatos',
            name='UCI',
            field=models.CharField(choices=[('2', 'no'), ('98', 'se ignora'), ('97', 'no aplica'), ('1', 'si'), ('99', 'no especificado')], default='1', max_length=2),
        ),
    ]
