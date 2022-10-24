# Generated by Django 4.0.5 on 2022-10-24 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('INTERFACE', '0027_delete_missionsview'),
    ]

    operations = [
        migrations.CreateModel(
            name='MissionsView',
            fields=[
                ('mission_id', models.CharField(db_column='Mission ID', max_length=100, primary_key=True, serialize=False)),
                ('mission_detailled_name', models.TextField(blank=True, db_column='Mission detailled name', null=True)),
                ('regional_place', models.TextField(blank=True, db_column='Regional place', null=True)),
                ('start_date_yyyy_mm_dd_field', models.DateField(blank=True, db_column='Start date [yyyy-mm-dd]', null=True)),
                ('end_date_yyyy_mm_dd_field', models.DateField(blank=True, db_column='End date [yyyy-mm-dd]', null=True)),
                ('stations_range', models.CharField(blank=True, db_column='Stations range', max_length=100, null=True)),
                ('samples_range', models.CharField(blank=True, db_column='Samples range', max_length=100, null=True)),
                ('participants', models.TextField(blank=True, db_column='Participants', null=True)),
                ('associated_field_notebooks', models.CharField(blank=True, db_column='Associated field notebooks', max_length=100, null=True)),
                ('associated_project', models.CharField(blank=True, db_column='Associated project', max_length=100, null=True)),
            ],
            options={
                'db_table': 'missions_view',
                'managed': False,
            },
        ),
    ]
