from rest_framework import serializers
from app.models import *


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Student_details
        fields='__all__'