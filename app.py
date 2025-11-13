import requests

def obtenir_blague():
    """
    Interroge l'API JokeAPI pour récupérer une blague aléatoire.
    """
    url = "https://v2.jokeapi.dev/joke/Any"  
    params = {
        "lang": "en",
        "format": "json"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status() 
        data = response.json()

        if data["type"] == "single":
            print(f"\nsetup : {data['joke']}\n")
        else:
            print(f"\nsetup : {data['setup']}")
            print(f"punchline : {data['delivery']}\n")

    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération de la blague : {e}")

if __name__ == "__main__":
    obtenir_blague()