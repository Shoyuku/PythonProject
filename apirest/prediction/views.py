from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from prediction.models import Individual
from prediction.serializers import IndividualSerializer
from sklearn.externals import joblib
import recordlinkage as rl
import pandas as pd

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
def predict(request): # fonction de prediction qui predit la valeur is_match de l'objet envoye
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

def predict_isMatch(unscaled_data): # chargement du modele et prediction

    DF = pd.DataFrame(data = unscaled_data, index = [0])
    DF = DF.set_index(['id_1','id_2'])
    DF = DF.drop(labels ='is_match',axis=1)

    loaded_model = joblib.load('E:/Cours/S9/Python for Data Analysis/Projet/PythonProject/apirest/prediction/finalized_model.sav')

    is_match = loaded_model.predict(DF)[0]

    return is_match