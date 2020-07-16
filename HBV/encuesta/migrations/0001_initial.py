# Generated by Django 2.0.5 on 2020-07-15 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(db_column='id_categoria', primary_key=True, serialize=False)),
                ('descripcion_cat', models.CharField(db_column='descripcion_cat', max_length=100)),
            ],
            options={
                'db_table': 'categoria',
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id_depa', models.AutoField(db_column='id_depa', primary_key=True, serialize=False)),
                ('nombre_depa', models.CharField(db_column='nombre_depa', max_length=150)),
            ],
            options={
                'db_table': 'departamento',
            },
        ),
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id_encuesta', models.AutoField(db_column='id_encuesta', primary_key=True, serialize=False)),
                ('fecha', models.DateField(auto_now_add=True, db_column='fecha')),
                ('hora', models.TimeField(auto_now_add=True, db_column='hora')),
                ('fk_id_departamento', models.ForeignKey(db_column='fk_id_departamento', on_delete=django.db.models.deletion.CASCADE, to='encuesta.Departamento')),
            ],
            options={
                'db_table': 'encuesta',
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id_municipio', models.AutoField(db_column='id_municipio', primary_key=True, serialize=False)),
                ('nombre_muni', models.CharField(max_length=150)),
                ('fk_id_departamento', models.ForeignKey(blank=True, db_column='fk_id_departamento', null=True, on_delete=django.db.models.deletion.CASCADE, to='encuesta.Departamento')),
            ],
            options={
                'db_table': 'municipio',
            },
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id_pregunta', models.AutoField(db_column='id_pregunta', primary_key=True, serialize=False)),
                ('nombre_pre', models.CharField(db_column='nombre_pre', max_length=200)),
                ('fk_id_categoria', models.ForeignKey(db_column='fk_id_categoria', on_delete=django.db.models.deletion.CASCADE, to='encuesta.Categoria')),
            ],
            options={
                'db_table': 'pregunta',
            },
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id_respuesta', models.AutoField(db_column='id_respuesta', primary_key=True, serialize=False)),
                ('valor', models.IntegerField(db_column='valor')),
                ('fk_id_encuesta', models.ForeignKey(blank=True, db_column='fk_id_encuesta', null=True, on_delete=django.db.models.deletion.CASCADE, to='encuesta.Encuesta')),
                ('fk_id_pregunta', models.ForeignKey(db_column='fk_id_pregunta', on_delete=django.db.models.deletion.CASCADE, to='encuesta.Pregunta')),
            ],
            options={
                'db_table': 'respuesta',
            },
        ),
        migrations.AddField(
            model_name='encuesta',
            name='fk_id_municipio',
            field=models.ForeignKey(db_column='fk_id_municipio', on_delete=django.db.models.deletion.CASCADE, to='encuesta.Municipio'),
        ),
    ]
