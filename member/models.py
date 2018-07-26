from django.db import models
from transaction.models import Deposit

# Create your models here.
class Member(models.Model):
	account_id = models.IntegerField()
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100, unique=True)
	pin = models.IntegerField()
	address = models.TextField()
	gender = models.CharField(max_length=20)
	status = models.CharField(max_length=50)
	no_telp = models.IntegerField()

	def __init__(self):
		return self.nama
