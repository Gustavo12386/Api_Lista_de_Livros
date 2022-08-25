from distutils.command.upload import upload
from django.db import models
from uuid import uuid4

def upload_image_book(instance, filename):
    return f"{instance.id_book}-{filename}"

class Books(models.Model):
    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    realizado_em = models.IntegerField()
    estado = models.CharField(max_length=50)
    foto_livro = models.ImageField(upload_to=upload_image_book, blank=True, null=True)
    editora = models.CharField(max_length=255)
    create_at = models.DateField(auto_now_add=True)

