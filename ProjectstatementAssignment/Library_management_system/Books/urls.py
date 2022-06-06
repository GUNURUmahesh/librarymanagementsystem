from django.urls import path

from .views import *

urlpatterns = [
    path('AdminRegister/',AdminRegisterAPI.as_view(), name="registration for admin"),
    path('Adminlogin/',AdminLoginApi.as_view(), name="login the admin"),
    path('addingbookforAdminuser/',BookPostApi.as_view(), name="Addingbook for admin"),
    path('getallbookforAdminuser/',GetAllBooksApi.as_view(), name="getall books of admin user"),
    path('Updatebookforadminuser/<int:id>/', BookUpdateApi.as_view()),
    path('DeleteBookforadminuser/<int:id>/', DeleteBook.as_view()),
]
