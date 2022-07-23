from rest_framework import serializers

from .models import Lead


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        read_only_fields = ("created_by", "created_at", "modifed_at")
        fields = "__all__"
