from django.db import models # type: ignore

class Transaction(models.Model):
    text = models.CharField(max_length=255)
    predicted_category = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
