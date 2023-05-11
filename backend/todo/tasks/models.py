from django.db import models

    
class User(models.Model):
    
    USERNAME_FIELD = "id"
    REQUIRED_FIELDS = []
    is_anonymous = False
    is_authenticated = True
    is_active = True


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = ("Пользователь"))
    title = models.CharField(max_length=128, blank=False, null=False)
    description = models.TextField(null=True, blank=True)
    
    is_completed = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    