from django.db import models
import datetime
import os

#functions
def filepath(request, filename):
    filename = str(request.nome) +"_"+ str(request.sobrenome)  + "." + str(filename.split(".")[1])
    return os.path.join('uploads/' + str(filename.split(".")[1]), filename)

#Models
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField('Nome', max_length=2000)
    sobrenome = models.CharField('Sobrenome', max_length=2000)
    data_nasc = models.DateField('Data de Nascimento')
    is_admin = models.BooleanField('Admin', default=False)
    file = models.FileField(upload_to=filepath, default="")

    @property
    def idade(self):
        delta = datetime.now().date() - self.data_nasc
        return int(delta.days / 365.25)
