from rest_framework import serializers
from referrals.models import Organization, Equipment, Referral, Incident


class OrganizationSerializer(serializers.ModelSerializer):
    equipments = serializers.SerializerMethodField()
    referrals = serializers.SerializerMethodField()

    class Meta:
        model = Organization
        fields = "__all__"

    def get_equipments(self, obj):
        return EquipmentSerializer(obj.equipment_set.all(), many=True).data

    def get_referrals(self, obj):
        return ReferralSerializer(obj.referral_set.all(), many=True).data


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = "__all__"


class ReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referral
        fields = "__all__"


class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = "__all__"
