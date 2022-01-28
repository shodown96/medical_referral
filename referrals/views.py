from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from referrals.serializers import (
    Organization,
    Equipment,
    Referral,
    Incident,
    OrganizationSerializer,
    EquipmentSerializer,
    ReferralSerializer,
    IncidentSerializer,
)

# Create your views here.
class OrganizationListAPIView(ListAPIView):
    """
    This Lists all medical organizations available.
    """

    permission_classes = []
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class OrganizationCreateAPIView(CreateAPIView):
    """
    This creates a new Organization, only accessible to authenticated users.
    """

    permission_classes = [IsAuthenticated]
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class OrganizationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    This gets a single Organization, only accessible to admins
    """

    permission_classes = [IsAdminUser]
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class EquipmentListAPIView(ListAPIView):
    """
    This Lists all medical Equipments available to their respective organizations.
    """

    permission_classes = []
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class EquipmentCreateAPIView(CreateAPIView):
    """
    This creates a new Equipment, only accessible to authenticated users.
    """

    permission_classes = [IsAuthenticated]
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class EquipmentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    This gets a single Equipment, only accessible to admins
    """

    permission_classes = [IsAdminUser]
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class ReferralListAPIView(ListAPIView):
    """
    This Lists all Medical Referral made to various organizations.
    """

    permission_classes = []
    queryset = Referral.objects.all()
    serializer_class = ReferralSerializer


class ReferralCreateAPIView(CreateAPIView):
    """
    This creates a new Referral, only accessible to authenticated users.
    """

    permission_classes = [IsAuthenticated]
    queryset = Referral.objects.all()
    serializer_class = ReferralSerializer


class ReferralRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    This gets a single Referral, only accessible to admins
    """

    permission_classes = [IsAdminUser]
    queryset = Referral.objects.all()
    serializer_class = ReferralSerializer


class IncidentListAPIView(ListAPIView):
    """
    This Lists all medical incidents of patients.
    """

    permission_classes = []
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

    def get_queryset(self, request, *args, **kwargs):
        user = self.kwargs.get("user")
        if not user:
            return Incident.objects.all()
        return Incident.objects.filter(user=user)



class IncidentCreateAPIView(CreateAPIView):
    """
    This creates a new Incident.
    """

    permission_classes = [IsAuthenticated]
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer


class IncidentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    This gets a single Incident, only accessible to admins
    """

    permission_classes = [IsAdminUser]
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
