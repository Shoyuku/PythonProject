Cette API est développée sous Django Rest Framework.

L'objectif de cette API est de pouvoir gérer une base de données selon les informations et requêtes qui lui sont envoyées. 

L'API permet de pouvoir inserer, modifier, supprimer les objets dans la base mais aussi de prédire la variable 'is_match' lors de l'insertion.

Pour pouvoir lancer l'API, il lancer l'invite de commande et se placer dans le fichier où se trouve le fichier manage.py.
Pour le lancer, il faut entrer python manage.py runserver

Il est possible de pouvoir avoir accès aux données avec ces liens :
- http://127.0.0.1:8000/individuals/ permet de retourner tous les éléments dans la base de données.
- http://127.0.0.1:8000/individual/x/ permet de retourner l'élément x de la base.

Voici donc quelques exemples de requêtes à envoyer sur une autre invite de commande.
Requete POST pour inserer un element
curl -X POST -H "Content-Type:application/json" http://127.0.0.1:8000/individuals/ -d {\"id_1\":1,\"id_2\":2,\"cmp_fname_c1\":0.5,\"cmp_fname_c2\":0.5,\"cmp_lname_c1\":0.5,\"cmp_lname_c2\":0.5,\"cmp_sex\":1,\"cmp_bd\":1,\"cmp_bm\":1,\"cmp_by\":1,\"cmp_plz\":1,\"is_match\":false}

Requete PUT pour modifier un element
curl -X PUT -H "Content-Type:application/json" http://127.0.0.1:8000/individual/1/ -d {\"id_1\":1,\"id_2\":2,\"cmp_fname_c1\":0.5,\"cmp_fname_c2\":0.5,\"cmp_lname_c1\":0.5,\"cmp_lname_c2\":0.5,\"cmp_sex\":1,\"cmp_bd\":1,\"cmp_bm\":1,\"cmp_by\":1,\"cmp_plz\":1,\"is_match\":true}

Requêtes DELETE pour supprimer un element
curl -X DELETE -H "Content-Type:application/json" http://127.0.0.1:8000/individual/1/

Requêtes POST pour inserer un element et le classifier
curl -X POST -H "Content-Type:application/json" http://127.0.0.1:8000/predict/ -d {\"id_1\":1,\"id_2\":2,\"cmp_fname_c1\":0.5,\"cmp_fname_c2\":0.5,\"cmp_lname_c1\":0.5,\"cmp_lname_c2\":0.5,\"cmp_sex\":1,\"cmp_bd\":1,\"cmp_bm\":1,\"cmp_by\":1,\"cmp_plz\":1,\"is_match\":false}

curl -X POST -H "Content-Type:application/json" http://127.0.0.1:8000/predict/ -d {\"id_1\":54009,\"id_2\":87393,\"cmp_fname_c1\":0.6922,\"cmp_fname_c2\":0,\"cmp_lname_c1\":0.5,\"cmp_lname_c2\":0,\"cmp_sex\":1,\"cmp_bd\":1,\"cmp_bm\":1,\"cmp_by\":1,\"cmp_plz\":1,\"is_match\":false}
