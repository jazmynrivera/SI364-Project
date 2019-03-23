from django.db import models

# Create your models here.

class User(models.Model) :
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    username = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    date_created = models.CharField(max_length=128)

class Store(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class Date(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=19,decimal_places=10)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    date = models.ForeignKey(Date, on_delete=models.CASCADE)

    def __str__(self) :
        return self.name