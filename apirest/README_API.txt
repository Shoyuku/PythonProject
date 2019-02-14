Cette API est d�velopp�e sous Django Rest Framework.

L'objectif de cette API est de pouvoir g�rer une base de donn�es selon les informations et requ�tes qui lui sont envoy�es. 

L'API permet de pouvoir inserer, modifier, supprimer les objets dans la base mais aussi de pr�dire la variable 'is_match' lors de l'insertion.

Pour pouvoir lancer l'API, il lancer l'invite de commande et se placer dans le fichier o� se trouve le fichier manage.py.
Pour le lancer, il faut entrer python manage.py runserver

Il est possible de pouvoir avoir acc�s aux donn�es avec ces liens :
- http://127.0.0.1:8000/individuals/ permet de retourner tous les �l�ments dans la base de donn�es.
- http://127.0.0.1:8000/individual/x/ permet de retourner l'�l�ment x de la base.

Voici donc quelques exemples de requ�tes � envoyer sur une autre invite de commande.
Requete POST pour inserer un element
curl -X POST -H "Content-Type:application/json" http://127.0.0.1:8000/individuals/ -d {\"id_1\":1,\"id_2\":2,\"cmp_fname_c1\":0.5,\"cmp_fname_c2\":0.5,\"cmp_lname_c1\":0.5,\"cmp_lname_c2\":0.5,\"cmp_sex\":1,\"cmp_bd\":1,\"cmp_bm\":1,\"cmp_by\":1,\"cmp_plz\":1,\"is_match\":false}

Requete PUT pour modifier un element
curl -X PUT -H "Content-Type:application/json" http://127.0.0.1:8000/individual/1/ -d {\"id_1\":1,\"id_2\":2,\"cmp_fname_c1\":0.5,\"cmp_fname_c2\":0.5,\"cmp_lname_c1\":0.5,\"cmp_lname_c2\":0.5,\"cmp_sex\":1,\"cmp_bd\":1,\"cmp_bm\":1,\"cmp_by\":1,\"cmp_plz\":1,\"is_match\":true}

Requ�tes DELETE pour supprimer un element
curl -X DELETE -H "Content-Type:application/json" http://127.0.0.1:8000/individual/1/

Requ�tes POST pour inserer un element et le classifier
curl -X POST -H "Content-Type:application/json" http://127.0.0.1:8000/predict/ -d {\"id_1\":1,\"id_2\":2,\"cmp_fname_c1\":0.5,\"cmp_fname_c2\":0.5,\"cmp_lname_c1\":0.5,\"cmp_lname_c2\":0.5,\"cmp_sex\":1,\"cmp_bd\":1,\"cmp_bm\":1,\"cmp_by\":1,\"cmp_plz\":1,\"is_match\":false}

curl -X POST -H "Content-Type:application/json" http://127.0.0.1:8000/predict/ -d {\"id_1\":54009,\"id_2\":87393,\"cmp_fname_c1\":0.6922,\"cmp_fname_c2\":0,\"cmp_lname_c1\":0.5,\"cmp_lname_c2\":0,\"cmp_sex\":1,\"cmp_bd\":1,\"cmp_bm\":1,\"cmp_by\":1,\"cmp_plz\":1,\"is_match\":false}
