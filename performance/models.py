from django.db import models

# Create your models here.

class AddEmployee(models.Model):
	firstname = models.CharField(max_length=30)
	lastname = models.CharField(max_length=30)
	mailid = models.EmailField()
	password = models.CharField(max_length=30)
	dateofbirth=models.CharField(max_length=30)
	employeeid=models.CharField(max_length=30)
	joiningdate=models.CharField(max_length=30)
	phonenumber=models.CharField(max_length=30)
	branch=models.CharField(max_length=30)
	designation=models.CharField(max_length=30)
	possition=models.CharField(max_length=30)


class FeedbackForm(models.Model):
	employeeid=models.CharField(max_length=30)
	reviewer=models.CharField(max_length=30)
	date=models.CharField(max_length=30)
	feedback=models.CharField(max_length=500)
