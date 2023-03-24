from rest_framework import serializers


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=200)
    rol= serializers.IntegerField()
    city= serializers.CharField(max_length=200)
