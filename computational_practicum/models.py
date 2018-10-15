from django.db import models


class Post(models.Model):
    x0 = models.FloatField()
    y0 = models.FloatField()
    x = models.FloatField()
    n = models.FloatField()

    def publish(self):
        self.save()

    def __float__(self):
        return self.x0
