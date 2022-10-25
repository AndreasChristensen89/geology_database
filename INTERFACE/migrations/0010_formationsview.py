# Generated by Django 4.0.5 on 2022-10-24 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('INTERFACE', '0009_delete_formationsview'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormationsView',
            fields=[
                ('formation_id', models.CharField(db_column='Formation ID', max_length=100, primary_key=True, serialize=False)),
                ('formation_full_name', models.CharField(blank=True, db_column='Formation Full Name', max_length=100, null=True)),
                ('detailled_description', models.TextField(blank=True, db_column='Detailled description', null=True)),
                ('latest_age_or_highest_stage', models.CharField(blank=True, db_column='Latest Age Or Highest Stage', max_length=100, null=True)),
                ('earliest_age_or_lowest_stage', models.CharField(blank=True, db_column='Earliest Age Or Lowest Stage', max_length=100, null=True)),
            ],
            options={
                'db_table': 'formations_view',
                'managed': False,
            },
        ),
    ]