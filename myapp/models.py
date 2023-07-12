from django.db import models

class Cake(models.Model):
    name=models.CharField(max_length=200)
    price=models.CharField(max_length=50)
    layer=models.CharField(max_length=20)
    options=(
        ("round","round"),
        ("square","square"),
        ("heart","heart"),
        ("other","other")
    )
    shape=models.CharField(max_length=20,choices=options,default="round",null=True,blank=True)

    def __str__(self):
        return self.name
