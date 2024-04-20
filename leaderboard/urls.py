from django.urls import path
from .views import *

urlpatterns = [
    path("leaderboard/", leaderboard_view, name="leaderboard"),
    path("leaderboard/individual/", individual_leaderboard_view, name="individual_leaderboard"),
    path("leaderboard/team/", team_leaderboard_view, name="team_leaderboard"),
    path('teams/', list_teams, name='list_teams'),
    path('teams/create/', create_team, name='create_team'),
    path('teams/join/', join_team, name='join_team'),
    path('teams/leave/<int:team_id>/', leave_team, name='leave_team'),
    path('edit-leaderboard/', edit_leaderboard, name='edit_leaderboard'),
    path('edit-leaderboard/<int:pk>/', edit_leaderboard_detail, name='edit_leaderboard_detail'),
]