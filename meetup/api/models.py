from django.db import models
from markdown.extensions.headerid import unique


class Account(models.Model):
    user_id = models.AutoField(primary_key =True)
    name = models.CharField(max_length=20, db_index=True)
    gender = models.BooleanField(db_index=True)
    age = models.PositiveIntegerField()
    description = models.CharField(max_length=100)
    orientation = models.BooleanField(db_index=True)
    photo_link1 = models.URLField()
    photo_link2 = models.URLField(null=True)
    photo_link3 = models.URLField(null=True)
    photo_link4 = models.URLField(null=True)
    photo_link5 = models.URLField(null=True)
    photo_link6 = models.URLField(null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modify_time = models.DateTimeField(auto_now=True)


class Location(models.Model):
    user_id = models.PositiveIntegerField(primary_key =True)
    latitude = models.DecimalField(db_index=True, max_digits=10, decimal_places=4)
    longitude = models.DecimalField(db_index=True, max_digits=10, decimal_places=4)
    last_update_time = models.DateTimeField(auto_now=True)
    
class Match(models.Model):
    user_id = models.PositiveIntegerField(db_index=True)
    match_user_id = models.PositiveIntegerField(db_index=True)
    islike = models.BooleanField(default = False)
    class Meta:
        unique_together = ('user_id', 'match_user_id',)
