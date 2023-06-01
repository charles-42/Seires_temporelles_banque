
import requests

# L'API renvoie le MAE, MSE, MAPE pour le mois de mars

############################# TELEPHONE ###################

# Route pour tester vos données de telephone
endpoint_url = 'http://tsapi.hugceffnd5dnf6ba.westeurope.azurecontainer.io/predict_telephone'

"""
Votre fichier CSV peut contenir un couple Entite/Famille ou plusieurs
Il doit cependant posséder une valeur "Nombre_entrants_corrige" pour chaque date du mois de mars
Schéma: "date_appel"(str) ,"Entite" (str),"Famille" (str), "Nombre_entrants_corrige" (int)
"""

# Remplacez par votre fichier CSV
files = {"file":  open('telephone_test.csv', 'rb')}


# Send the request to the API endpoint
response = requests.get(endpoint_url,  files =files)

# Check if the request was successful
if response.status_code == 200:
    # Return the response JSON
    print(response.json())
    
else:

    # If the request failed, raise an exception with the error message
    raise Exception(f'Request failed with status code {response.status_code}: {response.text}')


############################# EMAIL ###################

endpoint_url = 'http://tsapi.hugceffnd5dnf6ba.westeurope.azurecontainer.io/predict_email'

"""
Votre fichier CSV peut contenir un couple Entite/instance ou plusieurs
Il doit cependant posséder une valeur "Nb_recus" pour chaque date du mois de mars
Schéma: "Date"(str) ,"Entite" (str),"instance" (str), "Nb_recus" (int)
"""


# Remplacez par votre fichier CSV
files = {"file":  open('email_test.csv', 'rb')}


# Send the request to the API endpoint
response = requests.get(endpoint_url,  files =files)


# Check if the request was successful
if response.status_code == 200:
    # Return the response JSON
    print(response.json())
    
else:

    # If the request failed, raise an exception with the error message
    raise Exception(f'Request failed with status code {response.status_code}: {response.text}')

