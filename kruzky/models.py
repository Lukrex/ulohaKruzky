from django.db import models

class Veduci(models.Model):
    meno = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)

    def __str__(self):
        return f"{self.meno} {self.email}"

class Kruzok(models.Model):
    nazov = models.CharField(max_length=100)
    den = models.CharField(max_length=32)
    miestnost = models.CharField(max_length=16)
    veduci = models.ForeignKey(Veduci, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nazov} {self.den} {self.miestnost} {self.veduci}"