import requests
from bs4 import BeautifulSoup

def search_web(query, num_results=10):
    # Construimos la URL de búsqueda en Google
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}&hl=es"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        )
    }

    # Realizamos la solicitud a Google
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Error: Google devolvió el código {response.status_code}")
        return []

    # Parseamos el contenido HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Extraemos resultados de búsqueda
    results = []
    for result in soup.find_all("div", class_="tF2Cxc")[:num_results]:
        try:
            title = result.find("h3").text
            link = result.find("a")["href"]
            snippet = result.find("span", class_="aCOpRe").text if result.find("span", class_="aCOpRe") else ""
            results.append({"title": title, "link": link, "snippet": snippet})
        except AttributeError:
            continue

    return results

# Ejemplo de uso
query = "noticias sobre inteligencia artificial"
results = search_web(query)

for idx, result in enumerate(results, 1):
    print(f"{idx}. {result['title']}")
    print(f"   {result['link']}")
    print(f"   {result['snippet']}")
