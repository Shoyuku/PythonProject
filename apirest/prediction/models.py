from django.db import models
    
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