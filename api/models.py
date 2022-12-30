from django.db import models

# Create your models here.


class request_model(models.Model):
    query = models.TextField()

    def __str__(self):
        return self.query
    
    
class results_model(models.Model):
    query_id = models.TextField()
    matched = models.TextField()
    scores = models.TextField()
    commands = models.TextField(default="")

    def __str__(self):
        return self.query