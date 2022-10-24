# Generated by Django 4.0.5 on 2022-10-24 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('INTERFACE', '0013_delete_analysisfissiontracksview'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalysisFissionTracksView',
            fields=[
                ('analysis_id', models.CharField(db_column='Analysis ID', max_length=100, primary_key=True, serialize=False)),
                ('material_sample_id', models.CharField(blank=True, db_column='Material Sample ID', max_length=100, null=True)),
                ('location_id', models.CharField(blank=True, db_column='Location ID', max_length=100, null=True)),
                ('decimal_latitude', models.CharField(blank=True, db_column='Decimal Latitude', max_length=100, null=True)),
                ('decimal_longitude', models.CharField(blank=True, db_column='Decimal Longitude', max_length=100, null=True)),
                ('elevation_in_meters', models.FloatField(blank=True, db_column='Elevation In Meters', null=True)),
                ('barometric_elevation_in_meters', models.FloatField(blank=True, db_column='Barometric Elevation in Meters', null=True)),
                ('verbatim_locality', models.TextField(blank=True, db_column='Verbatim Locality', null=True)),
                ('field_mission_id', models.CharField(blank=True, db_column='Field Mission ID', max_length=100, null=True)),
                ('analysed_by', models.TextField(blank=True, db_column='Analysed By', null=True)),
                ('sampling_date', models.DateField(blank=True, db_column='Sampling Date', null=True)),
                ('simple_lithology_description', models.CharField(blank=True, db_column='Simple Lithology Description', max_length=100, null=True)),
                ('alteration_facies', models.CharField(blank=True, db_column='Alteration Facies', max_length=100, null=True)),
                ('metamorphism_facies', models.CharField(blank=True, db_column='Metamorphism Facies', max_length=100, null=True)),
                ('formation', models.CharField(blank=True, db_column='Formation', max_length=100, null=True)),
                ('current_storage', models.TextField(blank=True, db_column='Current storage', null=True)),
                ('comment', models.TextField(blank=True, db_column='Comment', null=True)),
                ('n_grains', models.IntegerField(blank=True, db_column='N Grains', null=True)),
                ('ps', models.FloatField(blank=True, null=True)),
                ('ns', models.FloatField(blank=True, db_column='Ns', null=True)),
                ('pi', models.FloatField(blank=True, null=True)),
                ('ni', models.FloatField(blank=True, db_column='Ni', null=True)),
                ('pd', models.FloatField(blank=True, null=True)),
                ('nd', models.FloatField(blank=True, db_column='Nd', null=True)),
                ('px2', models.IntegerField(blank=True, db_column='PX2', null=True)),
                ('dispersion', models.FloatField(blank=True, db_column='Dispersion', null=True)),
                ('central_age_ma_field', models.FloatField(blank=True, db_column='Central age [Ma]', null=True)),
                ('number_1s_central_age_ma_field', models.FloatField(blank=True, db_column='1s central age [Ma]', null=True)),
                ('mtl_um_field', models.FloatField(blank=True, db_column='MTL [um]', null=True)),
                ('number_1s_mtl_um_field', models.FloatField(blank=True, db_column='1s MTL [um]', null=True)),
                ('n_lengths', models.IntegerField(blank=True, db_column='N lengths', null=True)),
                ('dpar_um_field', models.FloatField(blank=True, db_column='Dpar [um]', null=True)),
                ('number_1s_dpar_um_field', models.FloatField(blank=True, db_column='1s Dpar [um]', null=True)),
                ('u_ppm_field', models.FloatField(blank=True, db_column='U [ppm]', null=True)),
                ('location_on_gis', models.TextField(blank=True, db_column='Location on GIS', null=True)),
            ],
            options={
                'db_table': 'analysis_fission_tracks_view',
                'managed': False,
            },
        ),
    ]
