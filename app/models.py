from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Account(models.Model):
    idAccount = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
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

    department = models.CharField(max_length=12, choices=DEPARTMENT_CHOICES)

    YEAR_IN_SCHOOL_CHOICES = (
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    year_in_school = models.CharField(max_length=4, choices=YEAR_IN_SCHOOL_CHOICES)

    githubLink = models.URLField(max_length=200, null=True, blank=True)
    linkedInLink = models.URLField(max_length=200, null=True, blank=True)





class Group(models.Model):
    idGroup = models.AutoField(primary_key=True)
    nameGroup = models.CharField(max_length=42, unique=True)
    idAccountGroup = models.ForeignKey(Account, on_delete=models.CASCADE)

class Category(models.Model):
    idCat = models.AutoField(primary_key=True)
    nameCat = models.CharField(max_length=42)
    groupCat = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)

class Publication(models.Model):
    #AutoField auto increment ID
    idPubli = models.AutoField(primary_key=True)
    titlePubli = models.CharField(max_length=42)
    ContentPubli = models.TextField(max_length=420)
    datePublished = models.DateTimeField(default=timezone.now)
    idAccountPubli = models.ForeignKey(Account, on_delete=models.CASCADE,) #User au lieu de Account ?
    idCatPubli = models.ForeignKey(Category, on_delete=models.CASCADE)


class File(models.Model):
    idFile = models.AutoField(primary_key=True)
    nameFile = models.CharField(max_length=100)
    fileFile = models.FileField(upload_to='file/', max_length=100) #add where it should be upload
    idPubliFile = models.ForeignKey(Publication, on_delete=models.CASCADE)

class Comment(models.Model):
    idAccountC = models.ForeignKey(Account, on_delete=models.CASCADE)
    idPubliC = models.ForeignKey(Publication, on_delete=models.CASCADE)
    comment = models.TextField(max_length=420)
    commentDate = models.DateTimeField(default=timezone.now)

class Belong(models.Model):
    idAccountB = models.ForeignKey(Account, on_delete=models.CASCADE)
    idGroupB = models.ForeignKey(Group, on_delete=models.CASCADE)
    joinDate = models.DateTimeField(default=timezone.now)

class Join(models.Model):
    idAccountJ = models.ForeignKey(Account, on_delete=models.CASCADE)
    idGroupJ = models.ForeignKey(Group, on_delete=models.CASCADE)


