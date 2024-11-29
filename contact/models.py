from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)
    message = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"