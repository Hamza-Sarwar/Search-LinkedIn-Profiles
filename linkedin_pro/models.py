from django.contrib.postgres.search import SearchVectorField
from django.db import models


class Cities(models.Model):
    name = models.CharField(max_length=255)
    state = models.ForeignKey('States', models.DO_NOTHING)
    state_code = models.CharField(max_length=255)
    country = models.ForeignKey('Countries', models.DO_NOTHING)
    country_code = models.CharField(max_length=2)
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    flag = models.SmallIntegerField()
    wikidataid = models.CharField(db_column='wikiDataId', max_length=255, blank=True,
                                  null=True)  # Field name made lowercase.
    names_vector = SearchVectorField(null=True)  # new field

    class Meta:
        managed = False
        db_table = 'cities'


class Countries(models.Model):
    name = models.CharField(max_length=100)
    iso3 = models.CharField(max_length=3, blank=True, null=True)
    numeric_code = models.CharField(max_length=3, blank=True, null=True)
    iso2 = models.CharField(max_length=2, blank=True, null=True)
    phonecode = models.CharField(max_length=255, blank=True, null=True)
    capital = models.CharField(max_length=255, blank=True, null=True)
    currency = models.CharField(max_length=255, blank=True, null=True)
    currency_name = models.CharField(max_length=255, blank=True, null=True)
    currency_symbol = models.CharField(max_length=255, blank=True, null=True)
    tld = models.CharField(max_length=255, blank=True, null=True)
    native = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    subregion = models.CharField(max_length=255, blank=True, null=True)
    timezones = models.TextField(blank=True, null=True)
    translations = models.TextField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    emoji = models.CharField(max_length=191, blank=True, null=True)
    emojiu = models.CharField(db_column='emojiU', max_length=191, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()
    flag = models.SmallIntegerField()
    wikidataid = models.CharField(db_column='wikiDataId', max_length=255, blank=True,
                                  null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'countries'


class States(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Countries, models.DO_NOTHING)
    country_code = models.CharField(max_length=2)
    fips_code = models.CharField(max_length=255, blank=True, null=True)
    iso2 = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=191, blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()
    flag = models.SmallIntegerField()
    wikidataid = models.CharField(db_column='wikiDataId', max_length=255, blank=True,
                                  null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'states'


class LinkedinProfiles(models.Model):
    index = models.BigAutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    linkedin_id = models.TextField(blank=True, null=True)
    primary_email = models.TextField(blank=True, null=True)
    other_emails = models.TextField(blank=True, null=True)
    primary_number = models.TextField(blank=True, null=True)
    other_numbers = models.TextField(blank=True, null=True)
    linkedin_url = models.TextField(blank=True, null=True)
    full_address = models.TextField(blank=True, null=True)
    city = models.ForeignKey(Cities, models.DO_NOTHING, blank=True, null=True)
    state = models.ForeignKey(States, models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey(Countries, models.DO_NOTHING, blank=True, null=True)
    names_vector = SearchVectorField(null=True)  # new field

    class Meta:
        managed = False
        db_table = 'linkedin_profiles'

    @staticmethod
    def fetch(**kwargs):
        return LinkedinProfiles.objects.filter(**{k: v for k, v in kwargs.items() if v is not None or ''})[:500]
