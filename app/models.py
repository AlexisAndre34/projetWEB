from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class account(models.Model):
    idAccount = models.OneToOneField(User, on_delete=models.CASCADE)
    lastName = models.CharField(max_length=42)
    firstName = models.CharField(max_length=42)
    email = models.models.EmailField()
    birthDate = models.DateField()

    DEPARTMENT_CHOICES= (
        ('IG', 'IG'),
        ('GBA', 'GBA'),
        ('EGC', 'EGC'),
        ('MAT', 'MAT'),
        ('MEA', 'MEA'),
        ('MI', 'MI'),
        ('MSI', 'MSI'),
        ('SE', 'SE'),
        ('STE', 'STE'),
    )

    department = models.CharField(max_length=12, choices=DEPARTMENT_CHOICES, default=IG)

    YEAR_IN_SCHOOL_CHOICES = (
        ('A1', '1er année')
        ('A2', '2nd année')
        ('A3', '3eme année')
        ('A4', '4eme année')
        ('A5', '5eme année')
    )
    year_in_school = models.CharField(max_lentgh=12, choices=YEAR_IN_SCHOOL_CHOICES, default=A1)

    githubLink = models.URLField(max_length=200, null=True, blank=True)
    linkedInLink = models.CharField(max_length=200, null=True, blank=True)

class Publication(models.Model):
    #AutoField auto increment ID
    idPubli = models.AutoField(primary_key=True)
    TitlePubli = models.CharField(max_length=42)
    ContentPubli = models.TextField(max_length=420)
    datePublished = models.DateTimeField(default=timezone.now)
    idAccountPubli = models.ForeignKey(Account, on_delete=models.CASCADE,) #User au lieu de Account ?
    idCatPubli = models.ForeignKey(Group, on_delete=models.CASCADE)

class Group(models.Model):
    idGroup = models.AutoField(primary_key=True)
    NameGroup = models.CharField(max_length=42)


class category(models.Model):
    idCat = models.AutoField(primary_key=True)
    NameCat = models.CharField(max_length=42)

class File(models.Model):
    idFile = models.AutoField(primary_key)
    NameFile = models.CharField(max_length=100)
    fileFile = models.FileField(upload_to=, max_length=100) #add where it should be upload
    idPubliFile = models.Foreign_Key(Publication, on_delete=models.CASCADE)

class Comment(models.Model):
    idAccountC = models.ForeignKey(Account, on_delete=models.CASCADE)
    idPubliC = models.ForeignKey(Publication, on_delete=models.CASCADE)
    comment = models.TextField(max_length=420)
    commentDate = models.DateTimeField(default=timezone.now)

class Belong(models.Model):
    idAccountB = models.ForeignKey(Account, on_delete=models.CASCADE)
    idGroupB = models.ForeignKey(Group, on_delete=models.CASCADE)
    joinDate = models.DateTimeField(default=timezone.now)

class manage(models.Model):
    idAccountB = models.ForeignKey(Account, on_delete=models.CASCADE)
    idGroupB = models.ForeignKey(Group, on_delete=models.CASCADE)

