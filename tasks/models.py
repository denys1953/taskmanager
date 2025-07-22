from django.db import models

class Task(models.Model):
    STATUS_CHOISE = [
        ("LOW", "Low"),
        ("MEDIUM", "Medium"),
        ("HIGH", "High")
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    due_date = models.DateField(blank=True, null=True)
    priority = models.CharField(choices=STATUS_CHOISE, max_length=30, default="todo")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
