from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

# model for activities
class Activity(models.Model):
    # title string
    title = models.CharField(max_length=200)
    # description string
    description = models.TextField()
    # creator_id foreign key to custom user model
    creator_id = models.ForeignKey('User', on_delete=models.CASCADE)
    # location string
    location = models.CharField(max_length=200)
    # event_date date
    event_date = models.DateField()
    # created_at date
    created_at = models.DateField(auto_now_add=True)
    # activity_type fk to activity type model
    activity_type = models.ForeignKey('ActivityType', on_delete=models.CASCADE)
    # photo field string
    photo = models.CharField(max_length=200)


class ActivityType(models.Model):
    pass
  
  
class UserParticipates(models.Model):
    # user_id fk to custom user model
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    # activity_id fk to activity model
    activity_id = models.ForeignKey('Activity', on_delete=models.CASCADE)
   
    
class UserInterested(models.Model):
    # user_id fk to custom user model
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    # activity_id fk to activity model
    activity_id = models.ForeignKey('Activity', on_delete=models.CASCADE)
    
    
class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(max_length=10)


class itemColor(models.Model):
    pass
  
  
# model for teams
class Team(models.Model):
    name = models.CharField(max_length=200)
    leader = models.OneToOneField(User, on_delete=models.PROTECT, primary_key = True)

    def total_points(self):
        # Calculate the total points of all users in this team
        return self.userprofile_set.aggregate(total_points=Sum('points'))['total_points'] or 0
    
    
# model that extends User model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    points = models.IntegerField(default=0)