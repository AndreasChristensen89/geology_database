# Generated by Django 4.0.5 on 2022-10-24 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('INTERFACE', '0015_delete_contactsview'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactsView',
            fields=[
                ('contact_id', models.IntegerField(db_column='Contact ID', primary_key=True, serialize=False)),
                ('location_id', models.CharField(blank=True, db_column='Location ID', max_length=100, null=True)),
                ('contact_type', models.CharField(blank=True, db_column='Contact Type', max_length=100, null=True)),
                ('associated_lithologic_observation_1', models.IntegerField(blank=True, db_column='Associated lithologic observation 1', null=True)),
                ('associated_lithologic_observation_2', models.IntegerField(blank=True, db_column='Associated lithologic observation 2', null=True)),
                ('associated_measured_plane_id', models.IntegerField(blank=True, db_column='Associated measured plane ID', null=True)),
                ('contact_type_remarks', models.TextField(blank=True, db_column='Contact Type Remarks', null=True)),
                ('observation_determined_by', models.CharField(blank=True, db_column='Observation Determined By', max_length=100, null=True)),
                ('observation_date', models.DateField(blank=True, db_column='Observation Date', null=True)),
            ],
            options={
                'db_table': 'contacts_view',
                'managed': False,
            },
        ),
    ]