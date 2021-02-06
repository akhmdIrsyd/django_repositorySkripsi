# Create your models here.
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, post_delete, pre_save,pre_delete
from django.dispatch import receiver

from django.utils.translation import ugettext_lazy as _

from django.db import models,transaction
from django.core.validators import FileExtensionValidator
# Create your models here.


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'Mahasiswa'),
        (2, 'Dosen'),
        (3, 'Admin'),
    )

    user_type = models.PositiveIntegerField(choices=USER_TYPE_CHOICES, default=1)
    __original_mode = None

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.__original_mode = self.user_type


    def save(self,force_insert=False, force_update=False, *args, **kwargs):
        print(self.id)
        if self.user_type != self.__original_mode:
            #  then do this
            if self.user_type == 2:
                if self.id== None :
                    pass
                else:
                    dosenobj=dosen(username=self.username)
                    dosenobj.save()
                    m = mahasiswa.objects.get(nim=self.id)
                    m.nim = self
                    m.delete()
                
            elif self.user_type == 1:
                mahasiswa.objects.create(nim=self)
                m = dosen.objects.get(username=self.id)
                m.username = self
                m.delete()
        else:
            create_dosen()

        super(User, self).save(force_insert, force_update, *args, **kwargs)
        self.__original_mode = self.user_type
        
    
    
    
@receiver(post_save, sender=User)
def create_dosen(sender, instance, created,**kwargs):
    if created :
        if instance.user_type == 2:
            dosen.objects.create(username=instance)
        elif instance.user_type == 1:
            mahasiswa.objects.create(nim=instance)



    




def _upload_path(instance, filename):
    return instance.get_upload_path(filename)


def file_size(value):  # add this to some file where you can import it from
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MB.')


class fakultas(models.Model):
    nama_fakultas = models.CharField(max_length=50)

    def __str__(self):
        return str(self.nama_fakultas)

class jurusan(models.Model):
    nama_jurusan = models.CharField(max_length=50)
    id_fakultas = models.ForeignKey(fakultas, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.nama_jurusan)

class dosen(models.Model):
    nama = models.CharField(max_length=50, blank=True, null=True)
    username = models.OneToOneField(User, on_delete=models.CASCADE,  unique=True)
    id_jurusan = models.ForeignKey(
        jurusan, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return str(self.nama)

    
        









class mahasiswa(models.Model):
    nama = models.CharField(max_length=50, blank=True, null=True)
    nim = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    id_jurusan = models.ForeignKey(jurusan, on_delete=models.DO_NOTHING, blank=True, null=True)
    pembimbing1 = models.ForeignKey(dosen, related_name="pembimbing1",on_delete=models.DO_NOTHING,blank=True, null=True)
    pembimbing2 = models.ForeignKey(dosen, related_name="pembimbing2",on_delete=models.DO_NOTHING,blank=True, null=True)
    judul = models.CharField(max_length=150)
    abstrak = models.TextField(blank=True, null=True)
    abstract = models.TextField(blank=True, null=True)
    bab1 = models.FileField(upload_to=_upload_path, blank=True, null=True, validators=[FileExtensionValidator(['pdf']), file_size])
    bab2 = models.FileField(upload_to=_upload_path, blank=True, null=True, validators=[FileExtensionValidator(['pdf']), file_size])
    bab3 = models.FileField(upload_to=_upload_path, blank=True, null=True, validators=[FileExtensionValidator(['pdf']), file_size])
    bab4 = models.FileField(upload_to=_upload_path, blank=True, null=True, validators=[FileExtensionValidator(['pdf']), file_size])
    bab5 = models.FileField(upload_to=_upload_path, blank=True, null=True, validators=[FileExtensionValidator(['pdf']), file_size])
    daftar_pustaka = models.FileField(upload_to=_upload_path, blank=True, null=True, validators=[FileExtensionValidator(['pdf']), file_size])

    def get_upload_path(self, filename):
        return "uploads/"+str(self.nim.username)+"/"+filename
    def __str__(self):
        return str(self.nama)
