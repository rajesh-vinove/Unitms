from django.db import models


class Driver(models.Model):
    fullname = models.CharField(max_length=100, null=True, blank=True)
    home_address = models.TextField()


class PrimeMover(models.Model):
    pm_number = models.CharField(max_length=100, null=True, blank=True)
    brand = models.CharField(max_length=100, null=True, blank=True)
    driven_by = models.CharField(max_length=100, null=True, blank=True)
    parks_at = models.CharField(max_length=100, null=True, blank=True)


class JObOrder(models.Model):
    """
    It is container in class diagram so  i am just taking single field for creating foreign key
    """
    name = models.CharField(max_length=100, null=True, blank=True)


class Trip(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE,null=True)
    primemover = models.ForeignKey(PrimeMover, on_delete=models.CASCADE,null=True)
    jobOrder = models.ForeignKey(JObOrder, on_delete=models.CASCADE,null=True)
    startPoint = models.CharField(max_length=100, null=True, blank=True)
    endPoint = models.CharField(max_length=100, null=True, blank=True)
    planTime = models.DateTimeField(auto_now_add=True)
    planBy = models.CharField(max_length=100, null=True, blank=True)
    tripAcknowledged = models.DateTimeField(auto_now_add=True)
    remarks = models.CharField(max_length=255, blank=True)
    isActive = models.BooleanField(default=True)
    isRejected = models.BooleanField(default=False)
    createdBy = models.CharField(max_length=100, null=True, blank=True)
    createdTime = models.CharField(max_length=100, null=True, blank=True)
    subletTo = models.CharField(max_length=100, blank=True)


