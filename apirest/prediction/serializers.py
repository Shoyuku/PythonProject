from rest_framework import serializers
from prediction.models import Individual

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