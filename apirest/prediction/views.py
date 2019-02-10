from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from prediction.models import Individual
from prediction.serializers import IndividualSerializer

'''
@csrf_exempt
def house_list(request):
    if request.method == 'GET':
        houses = House.objects.all()
        serializer = HouseSerializer(houses, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = HouseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data , status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def house_detail(request, pk):
    try:
        house = House.objects.get(pk=pk)
    except House.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = HouseSerializer(house)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = HouseSerializer(house, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        house.delete()
        return HttpResponse(status=204)

@csrf_exempt
def predict(request):
    if request.method == 'GET':
        return JsonResponse(serializer.errors, status = 400)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = HouseSerializer(data=data)
        if serializer.is_valid():
            data["MEDV"] = predict_medv(data)
            serializer = HouseSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status=400)

def predict_medv(unscaled_data):
    colonnes = ['CRIM', 'ZN', 'INDUS', 'CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT','MEDV']

    medv = 1

    return medv
'''

#curl -X POST -H "Content-Type:application/json" http://127.0.0.1:8000/houses/ -d {\"CRIM\":0.02731,\"ZN\":0.0,\"INDUS\":7.07,\"CHAS\":0.0,\"NOX\":0.469,\"RM\":6.421,\"AGE\":78.9,\"DIS\":4.9671,\"RAD\":2.0,\"TAX\":242.0,\"PTRATIO\":17.8,\"B\":396.9,\"LSTAT\":9.14,\"MEDV\":-1}

# Requete POST pour inserer un element
#curl -X POST -H "Content-Type:application/json" http://127.0.0.1:8000/individuals/ -d {\"id_1\":1,\"id_2\":2,\"cmp_fname_c1\":0.5,\"cmp_fname_c2\":0.5,\"cmp_lname_c1\":0.5,\"cmp_lname_c2\":0.5,\"cmp_sex\":1,\"cmp_bd\":1,\"cmp_bm\":1,\"cmp_by\":1,\"cmp_plz\":1,\"is_match\":false}

# Requete PUT pour modifier un element
#curl -X PUT -H "Content-Type:application/json" http://127.0.0.1:8000/individual/1/ -d {\"id_1\":1,\"id_2\":2,\"cmp_fname_c1\":0.5,\"cmp_fname_c2\":0.5,\"cmp_lname_c1\":0.5,\"cmp_lname_c2\":0.5,\"cmp_sex\":1,\"cmp_bd\":1,\"cmp_bm\":1,\"cmp_by\":1,\"cmp_plz\":1,\"is_match\":false}

# Requete DELETE pour supprimer un element
#curl -X DELETE -H "Content-Type:application/json" http://127.0.0.1:8000/individual/2/

# Requete POST pour inserer un element et le classifier
#curl -X POST -H "Content-Type:application/json" http://127.0.0.1:8000/predict/ -d {\"id_1\":1,\"id_2\":2,\"cmp_fname_c1\":0.5,\"cmp_fname_c2\":0.5,\"cmp_lname_c1\":0.5,\"cmp_lname_c2\":0.5,\"cmp_sex\":1,\"cmp_bd\":1,\"cmp_bm\":1,\"cmp_by\":1,\"cmp_plz\":1,\"is_match\":false}

@csrf_exempt
def individual_list(request):
    if request.method == 'GET': # retourne toute la liste d'objets Individual dans la base
        individuals = Individual.objects.all()
        serializer = IndividualSerializer(individuals, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST': # poste un objet Individual
        data = JSONParser().parse(request)
        serializer = IndividualSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data , status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def individual_detail(request, pk):
    try:
        individual = Individual.objects.get(pk=pk)
    except Individual.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET': # retourne l'objet correspondant
        serializer = IndividualSerializer(individual)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT': # modifie l'objet correspondant
        data = JSONParser().parse(request)
        serializer = IndividualSerializer(individual, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE': # supprime l'objet correspondant
        individual.delete()
        return HttpResponse(status=204)
        
@csrf_exempt
def predict(request):
    if request.method == 'GET':
        return JsonResponse(serializer.errors, status = 400)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = IndividualSerializer(data=data)
        if serializer.is_valid():
            data["is_match"] = predict_isMatch(data)
            serializer = IndividualSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status=400)

def predict_isMatch(unscaled_data):
    colonnes = ['id_1','id_2','cmp_fname_c1','cmp_fname_c2','cmp_lname_c1','cmp_lname_c2','cmp_sex','cmp_bd','cmp_bm','cmp_by','cmp_plz','is_match']

    is_match = True

    return is_match