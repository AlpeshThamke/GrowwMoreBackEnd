from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    useremail = models.EmailField(max_length=100)
    balance = models.FloatField()

    def __str__(self):
        return self.username

class Stocks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    quantity = models.IntegerField()
    prices = models.FloatField()

    def __str__(self):
        return self.company
    

class Mutual(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    quantity = models.FloatField()
    prices = models.FloatField()

    def __str__(self):
        return self.company


class Gold(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    quantity = models.FloatField()
    prices = models.FloatField()

    def __str__(self):
        return self.company


class CompanyStocks(models.Model):
    Name = models.CharField(max_length=100)
    quantity = models.IntegerField()


class CompanyMutual(models.Model):
    Name = models.CharField(max_length=100)
    quantity = models.FloatField()


class CompanyGold(models.Model):
    Name = models.CharField(max_length=100)
    quantity = models.FloatField()

