from rest_framework import serializers
from prediction.models import Individual

'''
class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ('CRIM', 'ZN', 'INDUS', 'CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT','MEDV')

def create(self, validated_data):
    """Create and return a new `House` instance, given the validated data."""
    return House.objects.create(**validated_data)

def update(self, instance, validated_data):
    """"Update and return an existing `House` instance, given the validated data."""
    instance.CRIM = validated_data.get('CRIM' , instance.CRIM )
    instance.ZN = validated_data.get('ZN' , instance.ZN )
    instance.INDUS = validated_data.get('INDUS' , instance.INDUS )
    instance.CHAS = validated_data.get('CHAS' , instance.CHAS )
    instance.NOX = validated_data.get('NOX' , instance.NOX )
    instance.RM = validated_data.get('RM' , instance.RM )
    instance.AGE = validated_data.get('AGE' , instance.AGE )
    instance.DIS = validated_data.get('DIS' , instance.DIS )
    instance.RAD = validated_data.get('RAD' , instance.RAD )
    instance.TAX = validated_data.get('TAX' , instance.TAX )
    instance.PTRATIO = validated_data.get('PTRATIO' , instance.PTRATIO )
    instance.B = validated_data.get('B' , instance.B )
    instance.LSTAT = validated_data.get('LSTAT' , instance.LSTAT )
    #instance.MEDV = validated_data.get('MEDV' , instance.MEDV )
    instance.save()
    return instance
'''

class IndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Individual
        fields = ('id_1','id_2','cmp_fname_c1','cmp_fname_c2','cmp_lname_c1','cmp_lname_c2','cmp_sex','cmp_bd','cmp_bm','cmp_by','cmp_plz','is_match')

def create(self, validated_data):
    """Create and return a new `House` instance, given the validated data."""
    return Individual.objects.create(**validated_data)

def update(self, instance, validated_data):
    """"Update and return an existing `House` instance, given the validated data."""
    instance.id_1 = validated_data.get('id_1' , instance.id_1 )
    instance.id_2 = validated_data.get('id_2' , instance.id_2 )
    instance.cmp_fname_c1 = validated_data.get('cmp_fname_c1' , instance.cmp_fname_c1 )
    instance.cmp_fname_c2 = validated_data.get('cmp_fname_c2' , instance.cmp_fname_c2 )
    instance.cmp_lname_c1 = validated_data.get('cmp_lname_c1' , instance.cmp_lname_c1 )
    instance.cmp_lname_c2 = validated_data.get('cmp_lname_c2' , instance.cmp_lname_c2 )
    instance.cmp_sex = validated_data.get('cmp_sex' , instance.cmp_sex )
    instance.cmp_bd = validated_data.get('cmp_bd' , instance.cmp_bd )
    instance.cmp_bm = validated_data.get('cmp_bm' , instance.cmp_bm )
    instance.cmp_by = validated_data.get('cmp_by' , instance.cmp_by )
    instance.cmp_plz = validated_data.get('cmp_plz' , instance.cmp_plz )
    instance.save()
    return instance