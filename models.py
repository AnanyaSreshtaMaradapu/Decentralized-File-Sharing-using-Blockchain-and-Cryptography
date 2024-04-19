from django.db import models

# Create your models here.
class users(models.Model):
	name=models.CharField(max_length=149);
	email=models.CharField(max_length=149);
	password=models.CharField(max_length=149);
	phone=models.CharField(max_length=149);

class files(models.Model):
	transaction_id=models.CharField(max_length=149);
	sender_email=models.CharField(max_length=249);
	recipient_email=models.CharField(max_length=249);
	title=models.CharField(max_length=449);
	file=models.BinaryField()

class localfiles(models.Model):
	transaction_id=models.CharField(max_length=149);
	remail=models.CharField(max_length=149);
	title=models.CharField(max_length=449);
	file=models.TextField()


	

