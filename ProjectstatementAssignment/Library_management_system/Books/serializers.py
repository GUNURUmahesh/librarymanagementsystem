from django.apps import apps
from rest_framework import serializers
from .models import AdminModel,BookModel
from django.contrib.auth.hashers import make_password
class AdminRegSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminModel
        fields = ['Firstname', 'Lastname', 'Email', 'Username', 'Password', 'MobileNumber']
        extra_kwargs = {'Password': {'write_only': True}, }

    def create(self, validated_data):
        user = AdminModel.objects.create(Firstname=validated_data['Firstname'], Lastname=validated_data['Lastname'],
                                        Email=validated_data['Email'], Username=validated_data['Username'],
                                        Password=make_password(validated_data['Password']),
                                        MobileNumber=validated_data['MobileNumber'],)

        user.save()
        return user


class AdminLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminModel
        fields = ['Email', 'Password']
        extra_kwargs = {'Password': {'write_only': True}}

    def create(self, validated_data):
        user = AdminModel.objects.get(Email=validated_data['Email'])
        user.save()
        return user


class BookPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = "__all__"

    def create(self, validated_data):
        user = BookModel.objects.create(AuthorName=validated_data['AuthorName'],
                                        BookName=validated_data['BookName'],
                                        BookPublishedOn=validated_data['BookPublishedOn'],
                                        BookId=validated_data['BookId'], Status=validated_data['Status'],
                                        AdminId=validated_data['AdminId'] )

        user.save()
        return user

class BooksUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ['id','AuthorName', 'BookName', 'BookPublishedOn', 'BookId', 'Status', 'AdminId']

    # def create(self, validated_data):
    #     user = BookModel.objects.get(id=validated_data['id'])
    #     user.save()
    #     return user
