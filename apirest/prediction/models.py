from django.db import models
'''
class House(models.Model):
    CRIM = models.FloatField()
    ZN = models.FloatField()
    INDUS = models.FloatField()
    CHAS = models.FloatField()
    NOX = models.FloatField()
    RM = models.FloatField()
    AGE = models.FloatField()
    DIS = models.FloatField()
    RAD = models.FloatField()
    TAX = models.FloatField()
    PTRATIO = models.FloatField()
    B = models.FloatField()
    LSTAT = models.FloatField()
    MEDV = models.FloatField(null=True)
    created = models.DateTimeField(auto_now_add=True)

class Meta:
    ordering = ['created']
'''
    
class Individual(models.Model):
    id_1 = models.IntegerField()
    id_2 = models.IntegerField()
    cmp_fname_c1 = models.FloatField()
    cmp_fname_c2 = models.FloatField()
    cmp_lname_c1 = models.FloatField()
    cmp_lname_c2 = models.FloatField()
    cmp_sex = models.IntegerField()
    cmp_bd = models.IntegerField()
    cmp_bm = models.IntegerField()
    cmp_by = models.IntegerField()
    cmp_plz = models.IntegerField()
    is_match = models.BooleanField()