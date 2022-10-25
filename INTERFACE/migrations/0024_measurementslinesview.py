# Generated by Django 4.0.5 on 2022-10-24 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('INTERFACE', '0023_delete_measurementslinesview'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeasurementsLinesView',
            fields=[
                ('measurement_id', models.IntegerField(db_column='Measurement ID', primary_key=True, serialize=False)),
                ('location_id', models.CharField(blank=True, db_column='Location ID', max_length=100, null=True)),
                ('decimal_longitude', models.FloatField(blank=True, db_column='Decimal Longitude', null=True)),
                ('decimal_latitude', models.FloatField(blank=True, db_column='Decimal Latitude', null=True)),
                ('geodetic_datum', models.CharField(blank=True, db_column='Geodetic datum', max_length=100, null=True)),
                ('northing_in_meters', models.DecimalField(blank=True, db_column='Northing in Meters', decimal_places=65535, max_digits=65535, null=True)),
                ('easting_in_meters', models.DecimalField(blank=True, db_column='Easting in Meters', decimal_places=65535, max_digits=65535, null=True)),
                ('georeferenced_by', models.CharField(blank=True, db_column='Georeferenced By', max_length=100, null=True)),
                ('elevation_in_meters', models.FloatField(blank=True, db_column='Elevation in Meters', null=True)),
                ('barometric_elevation_in_meters', models.FloatField(blank=True, db_column='Barometric Elevation in Meters', null=True)),
                ('georeferenced_local_date', models.DateField(blank=True, db_column='Georeferenced Local Date', null=True)),
                ('georeferenced_local_time', models.TimeField(blank=True, db_column='Georeferenced Local Time', null=True)),
                ('time_zone', models.CharField(blank=True, db_column='Time Zone', max_length=100, null=True)),
                ('verbatim_locality', models.TextField(blank=True, db_column='Verbatim Locality', null=True)),
                ('mission_detailled_name', models.TextField(blank=True, db_column='Mission Detailled Name', null=True)),
                ('formation_full_name', models.CharField(blank=True, db_column='Formation Full Name', max_length=100, null=True)),
                ('line_type', models.CharField(blank=True, db_column='Line type', max_length=100, null=True)),
                ('trend', models.SmallIntegerField(blank=True, db_column='Trend', null=True)),
                ('plunge', models.SmallIntegerField(blank=True, db_column='Plunge', null=True)),
                ('fault_movement_sense', models.CharField(blank=True, db_column='Fault Movement Sense', max_length=100, null=True)),
                ('measurement_accuracy', models.CharField(blank=True, db_column='Measurement Accuracy', max_length=100, null=True)),
                ('measurement_determined_date', models.DateField(blank=True, db_column='Measurement Determined Date', null=True)),
                ('measurement_determined_by', models.TextField(blank=True, db_column='Measurement Determined By', null=True)),
                ('instrument_id', models.TextField(blank=True, db_column='Instrument ID', null=True)),
                ('location_on_gis', models.TextField(blank=True, db_column='Location on GIS', null=True)),
            ],
            options={
                'db_table': 'measurements_lines_view',
                'managed': False,
            },
        ),
    ]