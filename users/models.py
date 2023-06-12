from django.db import models


class Users(models.Model):
    user_id = models.IntegerField(auto_created=True, primary_key=True)
    email = models.CharField(max_length=50)
    mob_num = models.IntegerField(max_length=10)
    password = models.CharField(max_length=20)
