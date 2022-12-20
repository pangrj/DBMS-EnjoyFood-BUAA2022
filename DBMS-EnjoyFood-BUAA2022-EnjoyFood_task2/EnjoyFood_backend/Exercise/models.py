from django.db import models


# Create your models here.
class Exercise(models.Model):
    sp_name = models.CharField(max_length=20, null=False)
    sp_content = models.CharField(max_length=20, null=False)
    sp_difficulty = models.CharField(max_length=20, null=False)
    sp_calories = models.IntegerField(null=False)
    sp_time = models.IntegerField(null=False)

    def get_sp_id(self):
        return self.id
