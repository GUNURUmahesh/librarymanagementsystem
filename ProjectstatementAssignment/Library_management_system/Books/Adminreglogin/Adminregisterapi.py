from rest_framework import generics
from rest_framework.decorators import parser_classes
from rest_framework.response import Response
from ..serializers import AdminRegSerializer
from rest_framework.parsers import MultiPartParser

@parser_classes((MultiPartParser,))
class AdminRegisterAPI(generics.GenericAPIView):
    serializer_class = AdminRegSerializer

    def post(self, request, *args, **kwargs):
        try:
            print("hai")
            serializer = self.get_serializer(data=request.data)
            print("hai2")
            serializer.is_valid(raise_exception=True)
            print("hai3")
            user = serializer.save()
            print("hai4")
            return Response({
                'message': 'Successful',
                'Result': AdminRegSerializer(user).data,
                'HasError': False,
                'status': 200
            })
        except Exception as e:
            return Response({
                'message': 'Fail',
                'Result': [],
                'HasError': True,
                'status': 400
            })