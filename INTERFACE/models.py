# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AnalysisAr(models.Model):
    analysis_id = models.CharField(db_column='Analysis ID', primary_key=True, max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    material_sample_id = models.ForeignKey('Samples', models.DO_NOTHING, db_column='Material Sample ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    number_36ar_fv_field = models.FloatField(db_column='36Ar [fV]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    uncertainty_36ar_1s_field = models.FloatField(db_column='uncertainty 36Ar [%1s] ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    number_37ar_fv_field = models.FloatField(db_column='37Ar [fV]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    uncerainty_37ar_1s_field = models.FloatField(db_column='uncerainty 37Ar [1s] ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    number_38ar_fv_field = models.FloatField(db_column='38Ar [fV]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    uncertainty_38ar_field = models.FloatField(db_column='uncertainty 38Ar [%] ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    number_39ar_fv_field = models.FloatField(db_column='39Ar [fV] ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    uncertainty_39ar_1s_field = models.FloatField(db_column='uncertainty 39Ar [1s] ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    number_40ar_fv_field = models.FloatField(db_column='40Ar [fV]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    number_1s_40ar_field = models.FloatField(db_column='1s 40Ar [%] ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    age_ma_field = models.FloatField(db_column='Age [Ma]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    uncertainty_age_2s_ma_field = models.FloatField(db_column='uncertainty Age [2s,Ma]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    number_40ar_field = models.FloatField(db_column='40Ar [%] ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    number_39ar_field = models.FloatField(db_column='39Ar [%]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    ca_k = models.FloatField(db_column='Ca/K', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    uncertainty_ca_k_1s_field = models.FloatField(db_column='uncertainty Ca/K [1s]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    cl_k = models.FloatField(db_column='Cl/K', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    uncertainty_cl_k_1s_field = models.FloatField(db_column='uncertainty Cl/K [1s]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'analysis_ar'


class AnalysisArArView(models.Model):
    analysis_id = models.CharField(primary_key=True, db_column='Analysis ID', max_length=100, blank=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    material_sample_id = models.CharField(db_column='Material Sample ID', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_id = models.CharField(db_column='Location ID', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    decimal_latitude = models.CharField(db_column='Decimal Latitude', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    decimal_longitude = models.CharField(db_column='Decimal Longitude', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    elevation_in_meters = models.FloatField(db_column='Elevation In Meters', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    verbatim_locality = models.TextField(db_column='Verbatim Locality', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_mission_id = models.CharField(db_column='Field Mission ID', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sampling_date = models.DateField(db_column='Sampling Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    simple_lithology_description = models.CharField(db_column='Simple Lithology Description', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    alteration_facies = models.CharField(db_column='Alteration Facies', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    metamorphism_facies = models.CharField(db_column='Metamorphism Facies', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    formation = models.CharField(db_column='Formation', max_length=100, blank=True, null=True)  # Field name made lowercase.
    current_storage = models.TextField(db_column='Current storage', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
    number_36ar_fv_field = models.FloatField(db_column='36Ar [fV]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    uncertainty_36ar_1s_field = models.FloatField(db_column='uncertainty 36Ar [%1s] ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    number_37ar_fv_field = models.FloatField(db_column='37Ar [fV]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    uncerainty_37ar_1s_field = models.FloatField(db_column='uncerainty 37Ar [1s] ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    number_38ar_fv_field = models.FloatField(db_column='38Ar [fV]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    uncertainty_38ar_field = models.FloatField(db_column='uncertainty 38Ar [%] ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    number_39ar_fv_field = models.FloatField(db_column='39Ar [fV] ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    uncertainty_39ar_1s_field = models.FloatField(db_column='uncertainty 39Ar [1s] ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    number_40ar_fv_field = models.FloatField(db_column='40Ar [fV]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    number_1s_40ar_field = models.FloatField(db_column='1s 40Ar [%] ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    age_ma_field = models.FloatField(db_column='Age [Ma]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    uncertainty_age_2s_ma_field = models.FloatField(db_column='uncertainty Age [2s,Ma]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    number_40ar_field = models.FloatField(db_column='40Ar [%] ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    number_39ar_field = models.FloatField(db_column='39Ar [%]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    ca_k = models.FloatField(db_column='Ca/K', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    uncertainty_ca_k_1s_field = models.FloatField(db_column='uncertainty Ca/K [1s]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    cl_k = models.FloatField(db_column='Cl/K', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    uncertainty_cl_k_1s_field = models.FloatField(db_column='uncertainty Cl/K [1s]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    location_on_gis = models.TextField(db_column='Location on GIS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'analysis_ar_ar_view'


class AnalysisFissionFracksView(models.Model):
    analysis_id = models.CharField(primary_key=True, db_column='Analysis ID', max_length=100, blank=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    material_sample_id = models.CharField(db_column='Material Sample ID', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_id = models.CharField(db_column='Location ID', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    decimal_latitude = models.CharField(db_column='Decimal Latitude', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    decimal_longitude = models.CharField(db_column='Decimal Longitude', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    elevation_in_meters = models.FloatField(db_column='Elevation In Meters', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    verbatim_locality = models.TextField(db_column='Verbatim Locality', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_mission_id = models.CharField(db_column='Field Mission ID', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sampling_date = models.DateField(db_column='Sampling Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    simple_lithology_description = models.CharField(db_column='Simple Lithology Description', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    alteration_facies = models.CharField(db_column='Alteration Facies', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    metamorphism_facies = models.CharField(db_column='Metamorphism Facies', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    formation = models.CharField(db_column='Formation', max_length=100, blank=True, null=True)  # Field name made lowercase.
    current_storage = models.TextField(db_column='Current storage', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    n_grains = models.IntegerField(db_column='N Grains', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ps = models.FloatField(blank=True, null=True)
    ns = models.FloatField(db_column='Ns', blank=True, null=True)  # Field name made lowercase.
    pi = models.FloatField(blank=True, null=True)
    ni = models.FloatField(db_column='Ni', blank=True, null=True)  # Field name made lowercase.
    pd = models.FloatField(blank=True, null=True)
    nd = models.FloatField(db_column='Nd', blank=True, null=True)  # Field name made lowercase.
    px2 = models.IntegerField(db_column='PX2', blank=True, null=True)  # Field name made lowercase.
    dispersion = models.FloatField(db_column='Dispersion', blank=True, null=True)  # Field name made lowercase.
    central_age_ma_field = models.FloatField(db_column='Central age [Ma]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    number_1s_central_age_ma_field = models.FloatField(db_column='1s central age [Ma]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    mtl_um_field = models.FloatField(db_column='MTL [um]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    number_1s_mtl_um_field = models.FloatField(db_column='1s MTL [um]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    n_lengths = models.IntegerField(db_column='N lengths', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dpar_um_field = models.FloatField(db_column='Dpar [um]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    number_1s_dpar_um_field = models.FloatField(db_column='1s Dpar [um]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    u_ppm_field = models.FloatField(db_column='U [ppm]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    location_on_gis = models.TextField(db_column='Location on GIS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'analysis_fission_fracks_view'


class AnalysisFt(models.Model):
    analysis_id = models.CharField(db_column='Analysis ID', primary_key=True, max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    material_sample_id = models.ForeignKey('Samples', models.DO_NOTHING, db_column='Material Sample ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    n_grains = models.IntegerField(db_column='N Grains', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ps = models.FloatField(blank=True, null=True)
    ns = models.FloatField(db_column='Ns', blank=True, null=True)  # Field name made lowercase.
    pi = models.FloatField(blank=True, null=True)
    ni = models.FloatField(db_column='Ni', blank=True, null=True)  # Field name made lowercase.
    pd = models.FloatField(blank=True, null=True)
    nd = models.FloatField(db_column='Nd', blank=True, null=True)  # Field name made lowercase.
    px2 = models.IntegerField(db_column='PX2', blank=True, null=True)  # Field name made lowercase.
    dispersion = models.FloatField(db_column='Dispersion', blank=True, null=True)  # Field name made lowercase.
    central_age_ma_field = models.FloatField(db_column='Central age [Ma]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    number_1s_central_age_ma_field = models.FloatField(db_column='1s central age [Ma]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    mtl_um_field = models.FloatField(db_column='MTL [um]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    number_1s_mtl_um_field = models.FloatField(db_column='1s MTL [um]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    n_lengths = models.IntegerField(db_column='N lengths', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dpar_um_field = models.FloatField(db_column='Dpar [um]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    number_1s_dpar_um_field = models.FloatField(db_column='1s Dpar [um]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    u_ppm_field = models.FloatField(db_column='U [ppm]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'analysis_ft'


class AnalysisUHeView(models.Model):
    analysis_id = models.CharField(primary_key=True, db_column='Analysis ID', max_length=100, blank=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    material_sample_id = models.CharField(db_column='Material Sample ID', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_id = models.CharField(db_column='Location ID', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    decimal_latitude = models.CharField(db_column='Decimal Latitude', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    decimal_longitude = models.CharField(db_column='Decimal Longitude', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    elevation_in_meters = models.FloatField(db_column='Elevation In Meters', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    verbatim_locality = models.TextField(db_column='Verbatim Locality', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_mission_id = models.CharField(db_column='Field Mission ID', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sampling_date = models.DateField(db_column='Sampling Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    simple_lithology_description = models.CharField(db_column='Simple Lithology Description', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    alteration_facies = models.CharField(db_column='Alteration Facies', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    metamorphism_facies = models.CharField(db_column='Metamorphism Facies', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    formation = models.CharField(db_column='Formation', max_length=100, blank=True, null=True)  # Field name made lowercase.
    current_storage = models.TextField(db_column='Current storage', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
    number_4he_nccstp_g_field = models.IntegerField(db_column='4He [nccSTP/g]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    number_238_u_ppm_field = models.FloatField(db_column='238_U [ppm]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    number_232_th_ppm_field = models.FloatField(db_column='232_Th [ppm]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    number_147_sm_ppm_field = models.FloatField(db_column='147_Sm [ppm]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    eu_ppm_field = models.FloatField(db_column='eU [ppm]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ft = models.FloatField(db_column='FT', blank=True, null=True)  # Field name made lowercase.
    th_u = models.FloatField(db_column='Th/U', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    measured_age_ma_field = models.FloatField(db_column='Measured age [Ma]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    number_1s_measured_age_ma_field = models.FloatField(db_column='1s measured age  [Ma]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    corrected_age_ma_field = models.FloatField(db_column='Corrected age  [Ma]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    number_1s_corrected_age_ma_field = models.FloatField(db_column='1s corrected age  [Ma]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    mean_age_ma_field = models.FloatField(db_column='Mean age  [Ma]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    number_1s_mean_age_ma_field = models.FloatField(db_column='1s mean age  [Ma]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    location_on_gis = models.TextField(db_column='Location on GIS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'analysis_u_he_view'


class AnalysisUhe(models.Model):
    analysis_id = models.CharField(db_column='Analysis ID', primary_key=True, max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    material_sample_id = models.ForeignKey('Samples', models.DO_NOTHING, db_column='Material Sample ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    number_4he_nccstp_g_field = models.IntegerField(db_column='4He [nccSTP/g]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    number_238_u_ppm_field = models.FloatField(db_column='238_U [ppm]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    number_232_th_ppm_field = models.FloatField(db_column='232_Th [ppm]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    number_147_sm_ppm_field = models.FloatField(db_column='147_Sm [ppm]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    eu_ppm_field = models.FloatField(db_column='eU [ppm]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ft = models.FloatField(db_column='FT', blank=True, null=True)  # Field name made lowercase.
    th_u = models.FloatField(db_column='Th/U', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    measured_age_ma_field = models.FloatField(db_column='Measured age [Ma]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    number_1s_measured_age_ma_field = models.FloatField(db_column='1s measured age  [Ma]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    corrected_age_ma_field = models.FloatField(db_column='Corrected age  [Ma]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    number_1s_corrected_age_ma_field = models.FloatField(db_column='1s corrected age  [Ma]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    mean_age_ma_field = models.FloatField(db_column='Mean age  [Ma]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    number_1s_mean_age_ma_field = models.FloatField(db_column='1s mean age  [Ma]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    comment = models.CharField(db_column='Comment', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'analysis_uhe'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Contacts(models.Model):
    contact_id = models.IntegerField(db_column='Contact ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_id = models.ForeignKey('Locations', models.DO_NOTHING, db_column='Location ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    contact_type = models.ForeignKey('LexiconContactType', models.DO_NOTHING, db_column='Contact Type')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    associated_lithologic_observation_1 = models.ForeignKey('LithologyDescriptions', models.DO_NOTHING, related_name="associated_lithologic_observation_1", db_column='Associated lithologic observation 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    associated_lithologic_observation_2 = models.ForeignKey('LithologyDescriptions', models.DO_NOTHING, related_name="associated_lithologic_observation_2", db_column='Associated lithologic observation 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    associated_measured_plane_id = models.ForeignKey('Measurements', models.DO_NOTHING, db_column='Associated measured plane ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    contact_type_remarks = models.TextField(db_column='Contact Type Remarks', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    observation_determined_by = models.ForeignKey('Geologists', models.DO_NOTHING, db_column='Observation Determined By', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    observation_date = models.DateField(db_column='Observation Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'contacts'


class ContactsView(models.Model):
    contact_id = models.TextField(primary_key=True, db_column='Contact ID', blank=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_id = models.CharField(db_column='Location ID', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    decimal_longitude = models.FloatField(db_column='Decimal Longitude', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    decimal_latitude = models.FloatField(db_column='Decimal Latitude', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    elevation_in_meters = models.FloatField(db_column='Elevation In Meters', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    geodetic_datum = models.CharField(db_column='Geodetic datum', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    northing_in_meters = models.DecimalField(db_column='Northing in Meters', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    easting_in_meters = models.DecimalField(db_column='Easting in Meters', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    georeferenced_by = models.CharField(db_column='Georeferenced By', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    verbatim_locality = models.TextField(db_column='Verbatim Locality', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mission_detailled_name = models.TextField(db_column='Mission detailled name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    observation_determined_date = models.DateField(db_column='Observation Determined Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    observation_determined_by = models.TextField(db_column='Observation Determined By', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    contact_type = models.CharField(db_column='Contact Type', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lithology_1 = models.CharField(db_column='Lithology 1', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lithology_2 = models.CharField(db_column='Lithology 2', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    plane_type = models.CharField(db_column='Plane type', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    plane_orientation = models.TextField(db_column='Plane Orientation', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    contact_type_remarks = models.TextField(db_column='Contact Type Remarks', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'contacts_view'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FieldMissions(models.Model):
    mission_id = models.CharField(db_column='Mission ID', primary_key=True, max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mission_detailled_name = models.TextField(db_column='Mission Detailled Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    regional_place = models.TextField(db_column='Regional place', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    start_date = models.DateField(db_column='Start date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    end_date = models.DateField(db_column='End date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    stations_range = models.CharField(db_column='Stations range', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    samples_range = models.CharField(db_column='Samples range', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    geologists = models.TextField(db_column='Geologists', blank=True, null=True)  # Field name made lowercase.
    associated_field_notebooks = models.CharField(db_column='Associated field notebooks', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    associated_project = models.CharField(db_column='Associated project', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'field_missions'


class FieldMissionsView(models.Model):
    mission_name = models.TextField(db_column='Mission Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mission_id = models.CharField(primary_key=True, db_column='Mission ID', max_length=100, blank=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    regional_place = models.TextField(db_column='Regional place', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    start_date = models.DateField(db_column='Start date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    end_date = models.DateField(db_column='End date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    stations_range = models.CharField(db_column='Stations Range', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    samples_range = models.CharField(db_column='Samples Range', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    participants = models.TextField(db_column='Participants', blank=True, null=True)  # Field name made lowercase.
    field_notebooks = models.CharField(db_column='Field notebooks', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    associated_project = models.CharField(db_column='Associated project', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'field_missions_view'


class Formations(models.Model):
    formation_id = models.CharField(db_column='Formation ID', primary_key=True, max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    formation_full_name = models.CharField(db_column='Formation Full Name', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    detailled_description = models.TextField(db_column='Detailled description', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    latest_age_or_highest_stage = models.ForeignKey('LexiconInternationalChronostratigraphicChart', models.DO_NOTHING, related_name="latest_age_or_highest_stage", db_column='Latest Age Or Highest Stage', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    earliest_age_or_lowest_stage = models.ForeignKey('LexiconInternationalChronostratigraphicChart', models.DO_NOTHING, related_name="earliest_age_or_lowest_stage", db_column='Earliest Age Or Lowest Stage', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'formations'


class FormationsView(models.Model):
    formation_id = models.CharField(primary_key=True, db_column='Formation ID', max_length=100, blank=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    formation_full_name = models.CharField(db_column='Formation Full Name', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    detailled_description = models.TextField(db_column='Detailled description', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    latest_age_or_highest_stage = models.CharField(db_column='Latest Age Or Highest Stage', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    earliest_age_or_lowest_stage = models.CharField(db_column='Earliest Age Or Lowest Stage', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'formations_view'


class GeographyColumns(models.Model):
    f_table_catalog = models.TextField(db_collation='C', blank=True, null=True)  # This field type is a guess.
    f_table_schema = models.TextField(db_collation='C', blank=True, null=True)  # This field type is a guess.
    f_table_name = models.TextField(db_collation='C', blank=True, null=True)  # This field type is a guess.
    f_geography_column = models.TextField(db_collation='C', blank=True, null=True)  # This field type is a guess.
    coord_dimension = models.IntegerField(blank=True, null=True)
    srid = models.IntegerField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'geography_columns'


class Geologists(models.Model):
    id_geologist = models.CharField(db_column='ID Geologist', primary_key=True, max_length=4)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    geologist_full_name = models.TextField(db_column='Geologist full name')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    institution = models.CharField(db_column='Institution', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    orcid = models.CharField(db_column='ORCID', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'geologists'


class GeometryColumns(models.Model):
    f_table_catalog = models.CharField(max_length=256, db_collation='C', blank=True, null=True)
    f_table_schema = models.TextField(db_collation='C', blank=True, null=True)  # This field type is a guess.
    f_table_name = models.TextField(db_collation='C', blank=True, null=True)  # This field type is a guess.
    f_geometry_column = models.TextField(db_collation='C', blank=True, null=True)  # This field type is a guess.
    coord_dimension = models.IntegerField(blank=True, null=True)
    srid = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'geometry_columns'


# class ImgLocations(models.Model):
#     location_id = models.OneToOneField('self', models.DO_NOTHING, db_column='Location ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     img_1 = models.BinaryField(blank=True, null=True)
#     img_2 = models.BinaryField(blank=True, null=True)
#     img_3 = models.BinaryField(blank=True, null=True)
#     img_4 = models.BinaryField(blank=True, null=True)
#     img_5 = models.BinaryField(blank=True, null=True)
#     img_6 = models.BinaryField(blank=True, null=True)
#     img_7 = models.BinaryField(blank=True, null=True)
#     img_8 = models.BinaryField(blank=True, null=True)
#     img_9 = models.BinaryField(blank=True, null=True)
#     img_10 = models.BinaryField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'img_locations'


# class ImgSamples(models.Model):
#     material_sample_id = models.OneToOneField('self', models.DO_NOTHING, db_column='Material Sample ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     img_1 = models.BinaryField(blank=True, null=True)
#     img_2 = models.BinaryField(blank=True, null=True)
#     img_3 = models.BinaryField(blank=True, null=True)
#     img_4 = models.BinaryField(blank=True, null=True)
#     img_5 = models.BinaryField(blank=True, null=True)
#     img_6 = models.BinaryField(blank=True, null=True)
#     img_7 = models.BinaryField(blank=True, null=True)
#     img_8 = models.BinaryField(blank=True, null=True)
#     img_9 = models.BinaryField(blank=True, null=True)
#     img_10 = models.BinaryField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'img_samples'


# class ImgSamplesSections(models.Model):
#     sample_section_id = models.OneToOneField('self', models.DO_NOTHING, db_column='Sample Section ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     img_1 = models.BinaryField(blank=True, null=True)
#     img_2 = models.BinaryField(blank=True, null=True)
#     img_3 = models.BinaryField(blank=True, null=True)
#     img_4 = models.BinaryField(blank=True, null=True)
#     img_5 = models.BinaryField(blank=True, null=True)
#     img_6 = models.BinaryField(blank=True, null=True)
#     img_7 = models.BinaryField(blank=True, null=True)
#     img_8 = models.BinaryField(blank=True, null=True)
#     img_9 = models.BinaryField(blank=True, null=True)
#     img_10 = models.BinaryField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'img_samples_sections'


class Instruments(models.Model):
    instrument_id = models.CharField(db_column='Instrument ID', primary_key=True, max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    extended_name = models.TextField(db_column='Extended name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    serial_number = models.CharField(db_column='Serial Number', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'instruments'


class LayerStyles(models.Model):
    f_table_catalog = models.CharField(max_length=100, blank=True, null=True)
    f_table_schema = models.CharField(max_length=100, blank=True, null=True)
    f_table_name = models.CharField(max_length=100, blank=True, null=True)
    f_geometry_column = models.CharField(max_length=100, blank=True, null=True)
    stylename = models.TextField(blank=True, null=True)
    styleqml = models.TextField(blank=True, null=True)  # This field type is a guess.
    stylesld = models.TextField(blank=True, null=True)  # This field type is a guess.
    useasdefault = models.BooleanField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    owner = models.CharField(max_length=63, blank=True, null=True)
    ui = models.TextField(blank=True, null=True)  # This field type is a guess.
    update_time = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'layer_styles'


class LexiconAlterationFacies(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    label = models.CharField(max_length=100)
    definition = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lexicon_alteration_facies'


class LexiconContactType(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    label = models.CharField(max_length=100)
    definition = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lexicon_contact_type'


class LexiconConventionCodeMeasure(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    label = models.CharField(max_length=100)
    definition = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lexicon_convention_code_measure'


class LexiconEpsg(models.Model):
    id_epsg = models.IntegerField(primary_key=True)
    coord_ref_sys_name = models.CharField(max_length=100)
    coord_red_sys_kind = models.CharField(max_length=100, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    revision_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lexicon_epsg'


class LexiconFaultMovementSense(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    label = models.CharField(max_length=100)
    definition = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lexicon_fault_movement_sense'


class LexiconFaultSensCriterion(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    label = models.CharField(max_length=100)
    definition = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lexicon_fault_sens_criterion'


class LexiconFossils(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    label = models.CharField(max_length=100)
    definition = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lexicon_fossils'


class LexiconInternationalChronostratigraphicChart(models.Model):
    sorting_order = models.SmallIntegerField(primary_key=True)
    id_chronosystem = models.CharField(unique=True, max_length=100)
    label = models.CharField(max_length=100)
    rank = models.CharField(max_length=100)
    red = models.SmallIntegerField()
    green = models.SmallIntegerField()
    blue = models.SmallIntegerField()
    html = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'lexicon_international_chronostratigraphic_chart'
        unique_together = (('sorting_order', 'id_chronosystem'),)


class LexiconLineType(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    label = models.CharField(max_length=100)
    definition = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lexicon_line_type'


class LexiconMeasurementAccuracy(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    label = models.CharField(max_length=100)
    definition = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lexicon_measurement_accuracy'


class LexiconMetamorphicFacies(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    label = models.CharField(max_length=100)
    definition = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lexicon_metamorphic_facies'


class LexiconMinerals(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    ima_status = models.CharField(db_column='IMA status', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'lexicon_minerals'


class LexiconObsSiteType(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    label = models.CharField(max_length=100)
    definition = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lexicon_obs_site_type'


class LexiconParticleShape(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    label = models.CharField(max_length=100)
    definition = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lexicon_particle_shape'


class LexiconParticleType(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    label = models.CharField(max_length=100)
    definition = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lexicon_particle_type'


class LexiconPlanarPolarity(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    label = models.CharField(max_length=100)
    definition = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lexicon_planar_polarity'


class LexiconPlaneType(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    label = models.CharField(max_length=100)
    definition = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lexicon_plane_type'


class LexiconSampleAim(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    label = models.CharField(max_length=100)
    definition = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lexicon_sample_aim'


class LexiconSampleSectionType(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    label = models.CharField(max_length=100)
    definition = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lexicon_sample_section_type'


class LexiconSampleType(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    label = models.CharField(max_length=100)
    definition = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lexicon_sample_type'


class LexiconSimpleLithology(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    label = models.CharField(max_length=100)
    definition = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lexicon_simple_lithology'


class LexiconTimeZones(models.Model):
    id_time_zone = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    offset = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'lexicon_time_zones'


class LithologyDescriptionView(models.Model):
    description_lithology_id = models.TextField(db_column='Description Lithology ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_id = models.CharField(primary_key=True, db_column='Location ID', max_length=100, blank=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    decimal_longitude = models.FloatField(db_column='Decimal Longitude', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    decimal_latitude = models.FloatField(db_column='Decimal Latitude', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    elevation_in_meters = models.FloatField(db_column='Elevation In Meters', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    geodetic_datum = models.CharField(db_column='Geodetic datum', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    northing_in_meters = models.DecimalField(db_column='Northing in Meters', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    easting_in_meters = models.DecimalField(db_column='Easting in Meters', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    georeferenced_by = models.CharField(db_column='Georeferenced By', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    verbatim_locality = models.TextField(db_column='Verbatim Locality', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mission_detailled_name = models.TextField(db_column='Mission detailled name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    observation_determined_date = models.DateField(db_column='Observation Determined Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    observation_determined_by = models.TextField(db_column='Observation Determined By', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    formation = models.CharField(db_column='Formation', max_length=100, blank=True, null=True)  # Field name made lowercase.
    simple_lithology_description = models.CharField(db_column='Simple Lithology Description', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    detailled_lithology_description = models.TextField(db_column='Detailled Lithology Description', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    alteration_facies = models.CharField(db_column='Alteration Facies', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    metamorphism_facies = models.CharField(db_column='Metamorphism Facies', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    particle_type = models.CharField(db_column='Particle Type', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    particle_shape = models.CharField(db_column='Particle Shape', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rock_texture = models.CharField(db_column='Rock Texture', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    color_rock_patina = models.CharField(db_column='Color Rock Patina', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    color_rock_into_break = models.CharField(db_column='Color Rock Into Break', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fossils = models.CharField(db_column='Fossils', max_length=100, blank=True, null=True)  # Field name made lowercase.
    deformation = models.TextField(db_column='Deformation', blank=True, null=True)  # Field name made lowercase.
    minerals_assemblages = models.TextField(db_column='Minerals Assemblages', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lithologic_description_determined_by = models.TextField(db_column='Lithologic Description Determined By', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lithology_remarks = models.TextField(db_column='Lithology Remarks', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'lithology_description_view'


class LithologyDescriptions(models.Model):
    description_lithology_id = models.SmallIntegerField(db_column='Description Lithology ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_id = models.ForeignKey('Locations', models.DO_NOTHING, db_column='Location ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    simple_lithology_description = models.ForeignKey(LexiconSimpleLithology, models.DO_NOTHING, db_column='Simple Lithology Description', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    alteration_facies = models.ForeignKey(LexiconAlterationFacies, models.DO_NOTHING, db_column='Alteration Facies', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    metamorphism_facies = models.ForeignKey(LexiconMetamorphicFacies, models.DO_NOTHING, db_column='Metamorphism Facies', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    particle_type = models.CharField(db_column='Particle Type', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    particle_shape = models.ForeignKey(LexiconParticleShape, models.DO_NOTHING, db_column='Particle Shape', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rock_texture = models.CharField(db_column='Rock Texture', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    color_rock_patina = models.CharField(db_column='Color Rock Patina', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    color_rock_into_break = models.CharField(db_column='Color Rock Into Break', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fossils = models.ForeignKey(LexiconFossils, models.DO_NOTHING, db_column='Fossils', blank=True, null=True)  # Field name made lowercase.
    minerals_assemblages = models.TextField(db_column='Minerals Assemblages', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    formation = models.ForeignKey(Formations, models.DO_NOTHING, db_column='Formation', blank=True, null=True)  # Field name made lowercase.
    lithologic_description_determined_by = models.ForeignKey(Geologists, models.DO_NOTHING, db_column='Lithologic Description Determined By', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lithology_remarks = models.TextField(db_column='Lithology Remarks', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    deformation = models.TextField(db_column='Deformation', blank=True, null=True)  # Field name made lowercase.
    detailled_lithology_description = models.TextField(db_column='Detailled Lithology Description', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'lithology_descriptions'


class Locations(models.Model):
    location_id = models.CharField(db_column='Location ID', primary_key=True, max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    decimal_longitude = models.CharField(db_column='Decimal Longitude', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    decimal_latitude = models.CharField(db_column='Decimal Latitude', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    georeferenced_by = models.CharField(db_column='Georeferenced By', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    geodetic_datum = models.ForeignKey(LexiconEpsg, models.DO_NOTHING, db_column='Geodetic Datum', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    elevation_in_meters = models.FloatField(db_column='Elevation In Meters', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    barometric_elevation_in_meters = models.FloatField(db_column='Barometric Elevation in Meters', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    georeferenced_date_iso_8601_1_2019_field = models.CharField(db_column='Georeferenced Date (ISO 8601-1:2019)', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    time_zone = models.ForeignKey(LexiconTimeZones, models.DO_NOTHING, db_column='Time Zone', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    georeferenced_local_date = models.DateField(db_column='Georeferenced Local Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    georeferenced_local_time = models.TimeField(db_column='Georeferenced Local Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    verbatim_locality = models.TextField(db_column='Verbatim Locality', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_mission_id = models.ForeignKey(FieldMissions, models.DO_NOTHING, db_column='Field Mission ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    observation_site_type = models.ForeignKey(LexiconObsSiteType, models.DO_NOTHING, db_column='Observation site type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    azimuth_of_observation = models.SmallIntegerField(db_column='Azimuth Of Observation', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_remarks = models.TextField(db_column='Location Remarks', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'locations'


class LocationsView(models.Model):
    location_id = models.CharField(primary_key=True, db_column='Location ID', max_length=100, blank=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    decimal_longitude = models.FloatField(db_column='Decimal Longitude', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    decimal_latitude = models.FloatField(db_column='Decimal Latitude', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    elevation_in_meters = models.FloatField(db_column='Elevation In Meters', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    geodetic_datum = models.CharField(db_column='Geodetic datum', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    northing_in_meters = models.DecimalField(db_column='Northing in Meters', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    easting_in_meters = models.DecimalField(db_column='Easting in Meters', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    georeferenced_by = models.CharField(db_column='Georeferenced By', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    verbatim_locality = models.TextField(db_column='Verbatim Locality', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    georeferenced_local_date = models.DateField(db_column='Georeferenced Local Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    georeferenced_local_time = models.TimeField(db_column='Georeferenced Local Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    time_zone = models.CharField(db_column='Time Zone', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mission_detailled_name = models.TextField(db_column='Mission Detailled Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    observation_site_type = models.CharField(db_column='Observation site type', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    azimuth_of_the_osbervation = models.SmallIntegerField(db_column='Azimuth of the osbervation', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_remarks = models.TextField(db_column='Location Remarks', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_on_gis = models.TextField(db_column='Location on GIS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'locations_view'


class Measurements(models.Model):
    measurement_id = models.IntegerField(db_column='Measurement ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_id = models.ForeignKey(Locations, models.DO_NOTHING, db_column='Location ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    associated_lithologic_observation = models.ForeignKey(LithologyDescriptions, models.DO_NOTHING, db_column='Associated lithologic observation', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    formation = models.ForeignKey(Formations, models.DO_NOTHING, db_column='Formation', blank=True, null=True)  # Field name made lowercase.
    convention_code_measure = models.ForeignKey(LexiconConventionCodeMeasure, models.DO_NOTHING, db_column='Convention Code Measure', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    plane_type = models.ForeignKey(LexiconPlaneType, models.DO_NOTHING, db_column='Plane Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    planar_polarity_code = models.ForeignKey(LexiconPlanarPolarity, models.DO_NOTHING, db_column='Planar Polarity Code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    plane_dip_azimuth = models.SmallIntegerField(db_column='Plane dip azimuth', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    plane_strike = models.SmallIntegerField(db_column='Plane Strike', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    plane_dip = models.SmallIntegerField(db_column='Plane Dip', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    plane_dip_quadrant = models.CharField(db_column='Plane Dip Quadrant', max_length=2, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    plane_remarks = models.TextField(db_column='Plane Remarks', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    line_type = models.ForeignKey(LexiconLineType, models.DO_NOTHING, db_column='Line Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    line_pitch = models.SmallIntegerField(db_column='Line Pitch', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    line_pitch_quadrant = models.CharField(db_column='Line Pitch Quadrant', max_length=2, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    line_trend = models.SmallIntegerField(db_column='Line Trend', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    line_plunge = models.SmallIntegerField(db_column='Line Plunge', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    line_remarks = models.TextField(db_column='Line Remarks', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    shear_displacement_structure = models.ForeignKey(LexiconFaultSensCriterion, models.DO_NOTHING, db_column='Shear Displacement Structure', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fault_movement_sense = models.ForeignKey(LexiconFaultMovementSense, models.DO_NOTHING, db_column='Fault Movement Sense', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    measurement_determined_by = models.ForeignKey(Geologists, models.DO_NOTHING, db_column='Measurement Determined By', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    measurement_determined_date = models.DateField(db_column='Measurement Determined Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    instrument_id = models.ForeignKey(Instruments, models.DO_NOTHING, db_column='Instrument ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    measurement_accuracy = models.ForeignKey(LexiconMeasurementAccuracy, models.DO_NOTHING, db_column='Measurement Accuracy', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'measurements'


class MeasurementsLinesView(models.Model):
    measurement_id = models.CharField(primary_key=True, db_column='Measurement ID', max_length=100, blank=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_id = models.CharField(db_column='Location ID', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    decimal_longitude = models.FloatField(db_column='Decimal Longitude', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    decimal_latitude = models.FloatField(db_column='Decimal Latitude', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    elevation_in_meters = models.FloatField(db_column='Elevation In Meters', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    geodetic_datum = models.CharField(db_column='Geodetic datum', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    northing_in_meters = models.DecimalField(db_column='Northing in Meters', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    easting_in_meters = models.DecimalField(db_column='Easting in Meters', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    georeferenced_by = models.CharField(db_column='Georeferenced By', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    verbatim_locality = models.TextField(db_column='Verbatim Locality', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mission_detailled_name = models.TextField(db_column='Mission detailled name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    measurement_determined_date = models.DateField(db_column='Measurement Determined Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    measurement_determined_by = models.TextField(db_column='Measurement Determined By', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    instrument_id = models.TextField(db_column='Instrument ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    formation = models.CharField(db_column='Formation', max_length=100, blank=True, null=True)  # Field name made lowercase.
    line_type = models.CharField(db_column='Line type', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    trend = models.SmallIntegerField(db_column='Trend', blank=True, null=True)  # Field name made lowercase.
    plunge = models.SmallIntegerField(db_column='Plunge', blank=True, null=True)  # Field name made lowercase.
    fault_movement_sense = models.CharField(db_column='Fault Movement Sense', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    measurement_accuracy = models.CharField(db_column='Measurement Accuracy', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_on_gis = models.TextField(db_column='Location on GIS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'measurements_lines_view'


class MeasurementsPlanesView(models.Model):
    measurement_id = models.CharField(primary_key=True, db_column='Measurement ID', max_length=100, blank=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_id = models.CharField(db_column='Location ID', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    decimal_longitude = models.FloatField(db_column='Decimal Longitude', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    decimal_latitude = models.FloatField(db_column='Decimal Latitude', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    elevation_in_meters = models.FloatField(db_column='Elevation In Meters', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    geodetic_datum = models.CharField(db_column='Geodetic datum', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    northing_in_meters = models.DecimalField(db_column='Northing in Meters', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    easting_in_meters = models.DecimalField(db_column='Easting in Meters', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    georeferenced_by = models.CharField(db_column='Georeferenced By', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    verbatim_locality = models.TextField(db_column='Verbatim Locality', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mission_detailled_name = models.TextField(db_column='Mission detailled name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    measurement_determined_date = models.DateField(db_column='Measurement Determined Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    measurement_determined_by = models.TextField(db_column='Measurement Determined By', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    instrument_id = models.TextField(db_column='Instrument ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    formation = models.CharField(db_column='Formation', max_length=100, blank=True, null=True)  # Field name made lowercase.
    plane_type = models.CharField(db_column='Plane type', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    polarity = models.TextField(db_column='Polarity', blank=True, null=True)  # Field name made lowercase.
    dip = models.SmallIntegerField(db_column='Dip', blank=True, null=True)  # Field name made lowercase.
    azimuth = models.SmallIntegerField(db_column='Azimuth', blank=True, null=True)  # Field name made lowercase.
    measurement_accuracy = models.CharField(db_column='Measurement Accuracy', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_on_gis = models.TextField(db_column='Location on GIS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'measurements_planes_view'


class Notebooks(models.Model):
    station = models.CharField(db_column='Station', primary_key=True, max_length=100)  # Field name made lowercase.
    img_1 = models.BinaryField(blank=True, null=True)
    img_2 = models.BinaryField(blank=True, null=True)
    img_3 = models.BinaryField(blank=True, null=True)
    img_4 = models.BinaryField(blank=True, null=True)
    img_5 = models.BinaryField(blank=True, null=True)
    img_6 = models.BinaryField(blank=True, null=True)
    img_7 = models.BinaryField(blank=True, null=True)
    img_8 = models.BinaryField(blank=True, null=True)
    img_9 = models.BinaryField(blank=True, null=True)
    img_10 = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notebooks'


class SampleSectionsView(models.Model):
    sample_section_id = models.CharField(primary_key=True, db_column='Sample Section ID', max_length=100, blank=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_id = models.CharField(db_column='Location ID', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    decimal_longitude = models.FloatField(db_column='Decimal Longitude', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    decimal_latitude = models.FloatField(db_column='Decimal Latitude', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    elevation_in_meters = models.FloatField(db_column='Elevation In Meters', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    geodetic_datum = models.CharField(db_column='Geodetic datum', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    northing_in_meters = models.DecimalField(db_column='Northing in Meters', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    easting_in_meters = models.DecimalField(db_column='Easting in Meters', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    georeferenced_by = models.CharField(db_column='Georeferenced By', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    verbatim_locality = models.TextField(db_column='Verbatim Locality', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mission_detailled_name = models.TextField(db_column='Mission detailled name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sampling_date = models.DateField(db_column='Sampling Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    simple_lithology_description = models.CharField(db_column='Simple Lithology Description', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    detailled_lithology_description = models.TextField(db_column='Detailled Lithology Description', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thin_section_orientation = models.CharField(db_column='Thin Section Orientation', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    plane_type = models.CharField(db_column='Plane type', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    plane_orientation = models.TextField(db_column='Plane Orientation', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    line_type = models.CharField(db_column='Line Type', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    line_orientation = models.TextField(db_column='Line orientation', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    number_of_sections = models.SmallIntegerField(db_column='Number of sections', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    position_on_gis = models.TextField(db_column='Position on GIS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'sample_sections_view'


class Samples(models.Model):
    material_sample_id = models.CharField(db_column='Material Sample ID', primary_key=True, max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sampling_location_id = models.ForeignKey(Locations, models.DO_NOTHING, db_column='Sampling Location ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sample_type = models.ForeignKey(LexiconSampleType, models.DO_NOTHING, db_column='Sample Type')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    first_sample_aim = models.ForeignKey(LexiconSampleAim, models.DO_NOTHING, related_name="first_sample_aim", db_column='First Sample Aim', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    second_sample_aim = models.ForeignKey(LexiconSampleAim, models.DO_NOTHING, related_name="second_sample_aim", db_column='Second Sample Aim', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    associated_lithologic_observation = models.ForeignKey(LithologyDescriptions, models.DO_NOTHING, db_column='Associated Lithologic Observation', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    associated_formation = models.ForeignKey(Formations, models.DO_NOTHING, db_column='Associated Formation', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    associated_measure_id = models.ForeignKey(Measurements, models.DO_NOTHING, db_column='Associated Measure ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sampling_date = models.DateField(db_column='Sampling Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sampled_by = models.ForeignKey(Geologists, models.DO_NOTHING, db_column='Sampled By', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sample_remarks = models.TextField(db_column='Sample Remarks', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    storage = models.TextField(db_column='Storage', blank=True, null=True)  # Field name made lowercase.
    igsn = models.CharField(db_column='IGSN', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'samples'


class SamplesSections(models.Model):
    sample_section_id = models.CharField(db_column='Sample Section ID', primary_key=True, max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    material_sample_id = models.ForeignKey(Samples, models.DO_NOTHING, db_column='Material Sample ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sample_section_type = models.ForeignKey(LexiconSampleSectionType, models.DO_NOTHING, db_column='Sample Section Type')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    orientation = models.CharField(db_column='Orientation', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mineral_assemblage = models.CharField(db_column='Mineral Assemblage', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    texture = models.CharField(db_column='Texture', max_length=100, blank=True, null=True)  # Field name made lowercase.
    microtectonic_description = models.TextField(db_column='Microtectonic description', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    movement_sens = models.CharField(db_column='Movement sens', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    supplements = models.TextField(db_column='Supplements', blank=True, null=True)  # Field name made lowercase.
    sample_section_remarks = models.TextField(db_column='Sample Section Remarks', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    storage = models.CharField(db_column='Storage', max_length=100, blank=True, null=True)  # Field name made lowercase.
    number_of_sections = models.SmallIntegerField(db_column='Number of sections', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'samples_sections'


class SamplesView(models.Model):
    material_sample_id = models.CharField(db_column='Material Sample ID', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_id = models.CharField(primary_key=True, db_column='Location ID', max_length=100, blank=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    decimal_longitude = models.FloatField(db_column='Decimal Longitude', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    decimal_latitude = models.FloatField(db_column='Decimal Latitude', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    elevation_in_meters = models.FloatField(db_column='Elevation In Meters', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    geodetic_datum = models.CharField(db_column='Geodetic datum', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    northing_in_meters = models.DecimalField(db_column='Northing in Meters', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    easting_in_meters = models.DecimalField(db_column='Easting in Meters', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    georeferenced_by = models.CharField(db_column='Georeferenced By', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    verbatim_locality = models.TextField(db_column='Verbatim Locality', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mission_detailled_name = models.TextField(db_column='Mission detailled name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sampling_date = models.DateField(db_column='Sampling Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    measurement_determined_by = models.TextField(db_column='Measurement Determined By', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sample_type = models.CharField(db_column='Sample type', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    first_sample_aim = models.CharField(db_column='First Sample Aim', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    second_sample_aim = models.CharField(db_column='Second Sample Aim', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lithology_description = models.CharField(db_column='Lithology Description', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    alteration_facies = models.CharField(db_column='Alteration Facies', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    metamorphism_facies = models.CharField(db_column='Metamorphism Facies', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    formation = models.CharField(db_column='Formation', max_length=100, blank=True, null=True)  # Field name made lowercase.
    plane_type = models.CharField(db_column='Plane type', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    plane_orientation = models.TextField(db_column='Plane Orientation', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    line_type = models.CharField(db_column='Line type', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    line_orientation = models.TextField(db_column='Line Orientation', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sample_remarks = models.TextField(db_column='Sample Remarks', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    current_storage = models.TextField(db_column='Current storage', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_on_gis = models.TextField(db_column='Location on GIS', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'samples_view'


class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spatial_ref_sys'


class Test(models.Model):
    analysis_id = models.CharField(db_column='Analysis ID', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    material_sample_id = models.CharField(db_column='Material Sample ID', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    number_36ar_fv_field = models.FloatField(db_column='36Ar [fV]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    uncertainty_36ar_1s_field = models.FloatField(db_column='uncertainty 36Ar [%1s] ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    number_37ar_fv_field = models.FloatField(db_column='37Ar [fV]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    uncerainty_37ar_1s_field = models.FloatField(db_column='uncerainty 37Ar [1s] ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    number_38ar_fv_field = models.FloatField(db_column='38Ar [fV]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    uncertainty_38ar_field = models.FloatField(db_column='uncertainty 38Ar [%] ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    number_39ar_fv_field = models.FloatField(db_column='39Ar [fV] ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    uncertainty_39ar_1s_field = models.FloatField(db_column='uncertainty 39Ar [1s] ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    number_40ar_fv_field = models.FloatField(db_column='40Ar [fV]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    number_1s_40ar_field = models.FloatField(db_column='1s 40Ar [%] ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    age_ma_field = models.FloatField(db_column='Age [Ma]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    uncertainty_age_2s_ma_field = models.FloatField(db_column='uncertainty Age [2s,Ma]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    number_40ar_field = models.FloatField(db_column='40Ar [%] ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    number_39ar_field = models.FloatField(db_column='39Ar [%]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    ca_k = models.FloatField(db_column='Ca/K', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    uncertainty_ca_k_1s_field = models.FloatField(db_column='uncertainty Ca/K [1s]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    cl_k = models.FloatField(db_column='Cl/K', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    uncertainty_cl_k_1s_field = models.FloatField(db_column='uncertainty Cl/K [1s]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'test'
