from rest_framework import serializers

class datosSerializer(serializers.Serializer):
    disco = serializers.CharField(max_length=10)
    memoria = serializers.CharField(max_length=10)
    cpu = serializers.CharField(max_length=10)
