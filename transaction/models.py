from django.db import models
from member.models import Member

# Create your models here.
class Deposit(models.Model):
	account_id = models.OneToOneField(Member, related_name='rek_deposit')
	name = models.CharField(max_length=100)
	start_balance = models.DecimalField()
	deposit = models.DecimalField()
	end_balance = models.DecimalField()
	depo_date = models.DateTimeField(auto_now_add=True, auto_now=True)

	def __str__(self):
		return str(self.name)


class Withdraw(models.Model):
	account_id = models.OneToOneField(Member, related_name='rek_withdraw')
	name = models.CharField(max_length=100)
	start_balance = models.DecimalField()
	withdrawal = models.DecimalField()
	end_balance = models.DecimalField()
	wd_date = models.DateTimeField(auto_now=True, auto_now_add=True)

	def __str__(self):
		return str(self.name)

class Borrows(models.Model):
	account_id = models.OneToOneField(Member, related_name='rek_borrow')
	name = models.CharField(max_length=100)
	admin_fee = models.DecimalField()
	borrow_funds = models.DecimalField()
	margin = models.DecimalField()
	lending_period = models.IntegerField()
	principal = models.DecimalField()
	margin_inst = models.DecimalField()
	total_principal = models.DecimalField()
	total_borrow = models.DecimalField()
	br_date = models.DateTimeField(auto_now_add=True, auto_now=True)

	def __str__(self):
		return str(self.name)

# class Installment(models.Model):
# 	name_borrow = models.OneToOneField(Borrows, related_name='borrow_name')
# 	installment_to = models.IntegerField()
# 	installment_period = models.IntegerField()
# 	installment_remain = models.DecimalField()
	

