from django.db import models

# Create your models here.

class Crop(models.Model):
    name = models.CharField(max_length = 250)
    totalTimeInDays = models.IntegerField(blank=True,null = True)
    seedsCostperSqFeet = models.IntegerField(blank=True,null = True)
    fertilizerCostPerSqFeet = models.IntegerField(blank=True,null = True)
    landPreperationTimeInDays = models.IntegerField(blank=True,null = True)
    SeedingTimeInDays = models.IntegerField(blank=True,null = True)
    transplantationTimeInDays = models.IntegerField(blank=True,null = True)
    irrigationTimeInDays = models.IntegerField(blank=True,null = True)
    weedingTimeInDays = models.IntegerField(blank=True,null = True)
    fertilizingTimeInDays = models.IntegerField(blank=True,null = True)
    harvestingTimeInDays = models.IntegerField(blank=True,null = True)
    minwaterRequirementInMM = models.IntegerField(blank=True,null = True)
    maxwaterRequirementInMM = models.IntegerField(blank=True,null = True)
    minRainfallDuringIrrigationInMM = models.IntegerField(blank=True,null = True)
    maxRainfallDuringIrrigationInMM = models.IntegerField(blank=True,null = True)
    minTempInDays = models.IntegerField(blank=True,null = True)
    maxTempInDays = models.IntegerField(blank=True,null = True)



    def __str__(self):
        return self.name

class FarmersQuery(models.Model):
    crop = models.ForeignKey(Crop,on_delete = models.CASCADE)
    location = models.CharField(max_length = 250)
    areaInSquarefeets = models.IntegerField()
    budgetInRupees = models.IntegerField()
    stayStrict = models.BooleanField(default = False)
