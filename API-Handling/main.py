# Bibliothek importieren, um mit APIs zu "sprechen"
import requests

## Projektinformationen

# Name der Applikation
APP_Name = "Swipe2Watch"

# Key nicht hartcodiert, da Projekt auf Github präsentiert wird
API_KEY = input("Enter API Key: ")

# URL API
BASE_URL = "https://api.themoviedb.org/3"


## Kernfunktionalität

# Funktion, um beliebte Filme abzurufen
def get_popular_movies(api_key, base_url):
    # Ziel-URL definieren (popular movies)
    full_url = f"{base_url}/movie/popular"

    # Abfrageparameter aus der API-Doku
    params = {
        # key ist globaler Authentifizierungsparameter
        # und wird laut DOC für alle Anfragen benötigt
        "api_key": api_key,
        "language": "de-DE",
        "page": 1
    }


    try:
        # get-Methode aus Request-Bibliothek aufrufen
        # hiermit wird eine get-Anfrage an die Webadresse gesendet
        response = requests.get(full_url, params=params)
        # Statuscode der ANtwort überprüfen
        response.raise_for_status()
        # Wenn erfolreich, dann Antwort des Servers in Variable speichern
        # Speicherung als Dictionary
        data = response.json()
        # mit dem Schlüsselwort results aus der API-Doku
        # die gespeicherten gewünschten aufrufen
        return data.get("results", [])

    # spezifische request-Fehler abfangen
    # .exceptions ist ein Submodu von request, für alle möglichen Fehlertypen
    # Wenn ein Fehler vom Typ RequestException auftritt, wird dieser in einer Variable gespeichert
    except requests.exceptions.RequestException as error_details:
        print(f"Fehler beim Abrufen der Filme: {error_details}")
        return []

# Variable für die angezeigten Filme
movies = get_popular_movies(API_KEY, BASE_URL)

# Wenn movies nicht leer ist
if movies:
    print("5 beliebte Filme gefunden")
    # Iteration über die ersten fünf Filme
    for movie in movies[:5]:
        print(f"{movie['title']}")

else:
    print("Konnte keine Filme finden. Bitte API-Key und Internetverbindung prüfen")
