from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """ Searilizes a name field """
    name = serializers.CharField(max_length=10)
