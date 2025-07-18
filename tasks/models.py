from django.db import models

class Tasks(models.Model):
    STATUS_CHOISE = [
        ("todo", "To Do"),
        ("in_progress", "In Progress"),
        ("done", "Done")
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    choise = models.CharField(choices=STATUS_CHOISE, max_length=30, default="todo")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
