from django.shortcuts import render
from .Adminreglogin.Adminregisterapi import AdminRegisterAPI
from .Adminreglogin.Adminlogin import AdminLoginApi
from .Bookcrud.createentryforbook import BookPostApi
from .Bookcrud.getallentriesofbook import GetAllBooksApi
from .Bookcrud.updatebook import BookUpdateApi
from .Bookcrud.deletebook import DeleteBook
# Create your views here.
AdminRegisterAPI()
AdminLoginApi()
BookPostApi()
GetAllBooksApi()
BookUpdateApi()
DeleteBook()