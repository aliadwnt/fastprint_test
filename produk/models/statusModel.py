from django.db import models

class Status(models.Model):
    nama_status = models.CharField(max_length=50)

    def __str__(self):
        return self.nama_status
