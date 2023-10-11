from rest_framework import serializers


class SchoolSerializers(serializers.Serializer):
    name = serializers.CharField()
    number = serializers.IntegerField()
    address = serializers.CharField()


{
    "name":"Math",
    "number":1,
    "address":"Razakova 32"

}