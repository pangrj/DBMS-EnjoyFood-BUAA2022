from django.db import models


# Create your models here.

class User(models.Model):
    u_id = models.IntegerField(primary_key=True, null=False)
    u_password = models.CharField(max_length=20, null=False)
    u_name = models.CharField(max_length=20, null=True, unique=True)
    u_position = models.CharField(max_length=30, null=True)
    u_gender = models.BooleanField()
    u_email = models.EmailField()
    u_age = models.IntegerField(null=True)
    u_height = models.IntegerField(null=True)
    u_weight = models.IntegerField(null=True)
    u_avatar = models.FileField(upload_to='uploads/', null=True, verbose_name='头像')

    def get_u_id(self):
        return self.u_id

    def set_u_id(self, u_id):
        self.u_id = u_id

    def get_u_password(self):
        return self.u_password

    def set_u_password(self, u_password):
        self.u_password = u_password

    def get_u_name(self):
        return self.u_name

    def set_u_name(self, u_name):
        self.u_name = u_name

    def get_u_position(self):
        return self.u_position

    def set_u_position(self, u_position):
        self.u_position = u_position

    def get_u_gender(self):
        return self.u_gender

    def set_u_gender(self, u_gender):
        self.u_gender = u_gender

    def get_u_email(self):
        return self.u_email

    def set_u_email(self, u_email):
        self.u_email = u_email

    def get_u_avatar(self):
        return self.u_avatar

    def set_u_avatar(self, u_photo):
        self.u_avatar = u_photo

    def get_u_height(self):
        return self.u_height

    def set_u_height(self, height):
        self.u_height = height

    def get_u_weight(self):
        return self.u_weight

    def set_u_weight(self, u_weight):
        self.u_weight = u_weight
