from rest_framework.views import APIView

from mainapp.models import (
    School,
)
from mainapp.serializers import (
    SchoolSerializers,
)

from rest_framework.response import Response


class SchoolView(APIView):

    def post(self, request):
        serializers = SchoolSerializers(data=request.data)
        serializers.is_valid(raise_exception=True) data = serializers.validated_data name = data.get('name')
        number = data.get('number')
        address = data.get('address')
        school = School.objects.create(
            name=name, number=number, address=address
        )
        return Response(SchoolSerializers(instance=school, many=True).data)
    
    def get(self, request):
        school = School.objects.all()
        serializers = SchoolSerializers(instance=school, many=True).data

        return Response(serializers)