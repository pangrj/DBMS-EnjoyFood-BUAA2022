from django.db import models

from Plan.models import Plan
from User.models import User


# Create your models here.
class CommentPlan(models.Model):
    r_star = models.CharField(max_length=20, null=False)
    r_content = models.CharField(max_length=100, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, null=False)
    r_data = models.DateTimeField(null=False, auto_now=True)

    def get_r_id(self):
        return self.id
