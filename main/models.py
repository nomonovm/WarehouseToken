from django.contrib.auth.models import *
from django.core.validators import MinValueValidator
from django.db import models


class Bolim(models.Model):
    nom = models.CharField(max_length=200)

    def __str__(self):
        return self.nom


class Mahsulot(models.Model):
    nom = models.CharField(max_length=222)
    brend = models.CharField(max_length=222)
    narx1 = models.FloatField(validators=[MinValueValidator(0.0)])
    narx2 = models.FloatField(validators=[MinValueValidator(0.0)], blank=True, null=True)
    miqdor = models.FloatField(validators=[MinValueValidator(0.0)])
    olchov = models.CharField(max_length=10)
    oxirgi_sana = models.DateTimeField(blank=True, null=True)
    bolim = models.ForeignKey(Bolim, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nom


class Sotuvchi(models.Model):
    rasm = models.ImageField(upload_to="sotuvchi/", blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bolim = models.ForeignKey(Bolim, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username


class Mijoz(models.Model):
    ism = models.CharField(max_length=200)
    dokon = models.CharField(max_length=200)
    manzil = models.CharField(max_length=200)
    qarz = models.FloatField()
    tel = models.CharField(max_length=20)
    bolim = models.ForeignKey(Bolim, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.ism


class Sotuv(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    miqdor = models.FloatField(validators=[MinValueValidator(0.0)])
    sana = models.DateTimeField(auto_now_add=True)
    jami_summa = models.FloatField(validators=[MinValueValidator(0.0)])
    qarz = models.FloatField(validators=[MinValueValidator(0.0)])
    tolandi = models.FloatField(validators=[MinValueValidator(0.0)])
    bolim = models.ForeignKey(Bolim, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.mahsulot} {self.miqdor}"
