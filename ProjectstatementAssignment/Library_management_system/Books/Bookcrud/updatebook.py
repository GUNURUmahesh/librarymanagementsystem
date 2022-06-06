from rest_framework import generics
from rest_framework.decorators import parser_classes
from rest_framework.response import Response
from ..serializers import BooksUpdateSerializer
from ..models import BookModel


class BookUpdateApi(generics.GenericAPIView):
    serializer_class = BooksUpdateSerializer

    def put(self, request, *args,id):
        try:
            userdata = BookModel.objects.get(id=id)

            s = BooksUpdateSerializer(userdata, data=request.data)
            s.is_valid(raise_exception=True)
            s.save()

            return Response({
                'message': 'Successful',
                'Result': True,
                'HasError': False,
                'status': 200
            })
        except BookModel.DoesNotExist as e:
            return Response({
                'message': 'Not Updated',
                'Result':False,
                'HasError': True,
                'status': 400
            })
