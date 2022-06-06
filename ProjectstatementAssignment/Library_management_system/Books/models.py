from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
class AdminModel(models.Model):
    firstname_regex = RegexValidator(regex=r'^(?=.{2,12}$)(?![_.])(?!.*[_.]{2})[a-zA-Z]+(?<![_.])$',
                                     message="firstname "
                                             "must string and should not be less than 3 and greater than 12")
    lastname_regex = RegexValidator(regex=r'^(?=.{2,12}$)(?![_.])(?!.*[_.]{2})[a-zA-Z]+(?<![_.])$',
                                    message="lastname "
                                            "must string and should not be less than 3 and greater than 12")
    password_regex = RegexValidator(regex="^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$",
                                    message="password "
                                            "must contain 8 letters and a captail letter and a special character ")
    Firstname = models.CharField(validators=[firstname_regex], max_length=30)
    Lastname = models.CharField(validators=[lastname_regex], max_length=30)
    Email = models.EmailField(max_length=50,unique=True)
    Username = models.CharField(max_length=60, unique=True)
    Password = models.CharField(validators=[password_regex], max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 14 digits "
                                         "allowed.")
    MobileNumber = models.CharField(validators=[phone_regex], max_length=14, unique=True)
    objects = models.Manager

    class Meta:
        db_table = "User_Data"



class BookModel(models.Model):
    class Status(models.TextChoices):
        Borrowed = 'Borrowed'
        Avaliable = 'Avaliable'

    AuthorName = models.CharField(max_length=250)
    BookName = models.CharField(max_length=250)
    BookPublishedOn = models.CharField(max_length=250)
    BookId = models.CharField(max_length=250)
    Status = models.CharField(max_length=10, choices=Status.choices)
    AdminId = models.ForeignKey(AdminModel, related_name="LibraryId", on_delete=models.CASCADE)


    class Meta:
        db_table = "Book_Table"

