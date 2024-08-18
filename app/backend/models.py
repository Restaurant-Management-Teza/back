from django.db import models

# Create your models here.


class Table(models.Model):
    qr_code = models.CharField(max_length=255, null=False)
    status = models.BooleanField(default=False)
    assigned_waiter_id = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.id} - {self.status} - {self.assigned_waiter if self.assigned_waiter else 'No waiter assigned'}"


class Client(models.Model):
    pass


class Waiter(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    assigned_tables = models.ManyToManyField(Table, related_name='waiters')

    def __str__(self):
        return f"{self.first_name}, {self.last_name} - {self.assigned_tables}"
