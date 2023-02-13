from rest_framework import serializers
from .models import LinkedinProfiles, Cities, States, Countries


class ProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkedinProfiles
        # fields = ["name", "linkedin_url", "full_address", "city_id", "state_id", "country_id"]
        # exclude = ['names_vector']


class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = ["name", "state_id", "country_id"]


class StatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = States
        fields = ["name", "country_id"]


class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = States
        fields = ["id", "name"]
