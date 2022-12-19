from django.db import models


# Create your models here.
class LifeCircle(models.Model):
    c_name = models.CharField(max_length=20, null=False)
    c_location = models.CharField(max_length=20, null=False)
    c_description = models.CharField(max_length=20, null=False)

    def get_c_id(self):
        return self.id
