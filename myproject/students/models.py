from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True)
    id_proof = models.FileField(upload_to='id_proofs/')
    file_path = models.CharField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        # Set the file path dynamically based on the uploaded file
        if self.id_proof:
            self.file_path = self.id_proof.name
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
