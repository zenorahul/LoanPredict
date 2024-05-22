from django.db import models

# Create your models here.
class LoanDetails(models.Model):
    customer=models.CharField(max_length=90)
    file=models.FileField()
    income=models.IntegerField()
    loanamt=models.IntegerField()
    credits=models.IntegerField()
    loanterm=models.IntegerField()