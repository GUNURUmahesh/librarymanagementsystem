from django.contrib.auth.hashers import check_password
from rest_framework import generics
from rest_framework.decorators import parser_classes
from rest_framework.response import Response
from ..serializers import *
from ..models import *


class AdminLoginApi(generics.GenericAPIView):
    serializer_class = AdminLoginSerializer

    def post(self, request):
        try:
            Email = request.data.get('Email')
           # print(Email)
            password = request.data.get('Password')
           # print(password)
            userdata = AdminModel.objects.get(Email=Email)
            if userdata.Password == password:
                print("hai")
            return Response({
                'message': 'Successful',
                'Result': AdminRegSerializer(userdata).data,
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