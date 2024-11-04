from rest_framework import serializers


class ListLinksSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=200)
    link = serializers.CharField(max_length=250)

    def __str__(self):
        return self.name
