from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    target_role = models.CharField(max_length=150, blank=True, default='')
    bio = models.TextField(blank=True, default='')

    def __str__(self):
        return f"{self.user.email}'s profile"


class UserSkill(models.Model):
    PROFICIENCY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skills')
    skill_name = models.CharField(max_length=150)
    proficiency = models.CharField(max_length=20, choices=PROFICIENCY_CHOICES, default='intermediate')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'skill_name')

    def __str__(self):
        return f"{self.user.email} - {self.skill_name}"


class Analysis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='analyses')
    target_role = models.CharField(max_length=150)
    match_percentage = models.FloatField(default=0)
    matched_core = models.JSONField(default=list)
    missing_core = models.JSONField(default=list)
    matched_nice = models.JSONField(default=list)
    missing_nice = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.email} - {self.target_role} ({self.match_percentage}%)"