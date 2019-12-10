from django.db import models

# Create your models here.

class Crop(models.Model):
    name = models.CharField(max_length = 250)

    def __str__(self):
        return self.name

class FarmersQuery(models.Model):
    crop = models.ForeignKey(Crop,on_delete = models.CASCADE)
    location = models.CharField(max_length = 250)
    areaInSquarefeets = models.IntegerField()
    budgetInRupees = models.IntegerField()
    stayStrict = models.BooleanField(default = False)
