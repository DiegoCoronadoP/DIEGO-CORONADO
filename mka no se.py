# Importar bibliotecas necesarias
import requests
from bs4 import BeautifulSoup

# Definir una función que tome los datos del usuario como entrada
def buscar_trabajos(campo_trabajo, habilidades, cursos, experiencias, genero, edad):
    # Definir la URL de la página de búsqueda de trabajo
    url = "https://www.indeed.com/advanced_search"

    # Crear un diccionario para almacenar los parámetros de búsqueda
    parametros_busqueda = {
        "q": campo_trabajo,  # Título del trabajo
        "l": "",  # Ubicación (dejar en blanco para trabajos remotos)
        "radius": "25",  # Radio de búsqueda (millas)
        "start": "1",  # Página de inicio
        "sort": "date",  # Ordenar por fecha
        "jt": "all",  # Tipo de trabajo (todos)
        "fromage": "any",  # Desde edad (cualquiera)
        "toage": "any",  # Hasta edad (cualquiera)
        "fromexp": "any",  # Desde experiencia (cualquiera)
        "toexp": "any",  # Hasta experiencia (cualquiera)
        "fromedu": "any",  # Desde educación (cualquiera)
        "toedu": "any",  # Hasta educación (cualquiera)
        "fromsal": "any",  # Desde salario (cualquiera)
        "tosal": "any",  # Hasta salario (cualquiera)
        "advn": "true",  # Búsqueda avanzada
        "from": "advancedsearch"  # Desde búsqueda avanzada
    }

    # Agregar habilidades a los parámetros de búsqueda
    for habilidad in habilidades:
        parametros_busqueda[f"as_and={habilidad}"] = ""

    # Agregar cursos a los parámetros de búsqueda
    for curso in cursos:
        parametros_busqueda[f"as_and={curso}"] = ""

    # Agregar experiencias a los parámetros de búsqueda
    for experiencia in experiencias:
        parametros_busqueda[f"as_and={experiencia}"] = ""

    # Agregar género y edad a los parámetros de búsqueda
    parametros_busqueda["gender"] = genero
    parametros_busqueda["age"] = edad

    # Enviar una solicitud GET a la página de búsqueda de trabajo
    respuesta = requests.get(url, params=parametros_busqueda)

    # Analizar el contenido HTML usando BeautifulSoup
    sopa = BeautifulSoup(respuesta.content, "html.parser")

    # Extraer los anuncios de trabajo de la página
    anuncios_trabajo = sopa.find_all("div", {"class": "jobsearch-SerpJobCard"})

    # Imprimir los anuncios de trabajo
    for anuncio in anuncios_trabajo:
        print(anuncio.find("h2", {"class": "title"}).text)
        print(anuncio.find("span", {"class": "company"}).text)
        print(anuncio.find("span", {"class": "location"}).text)
        print(anuncio.find("span", {"class": "summary"}).text)
        print("")
    print(sopa.text)
# Obtener datos del usuario
campo_trabajo = input("Ingrese su campo de trabajo: ")
habilidades = input("Ingrese sus habilidades (separadas por comas): ").split(",")
cursos = input("Ingrese los cursos que ha tomado (separados por comas): ").split(",")
experiencias = input("Ingrese sus experiencias laborales (separadas por comas): ").split(",")
genero = input("Ingrese su género: ")
edad = int(input("Ingrese su edad: "))

# Buscar trabajos con los datos del usuario
buscar_trabajos(campo_trabajo, habilidades, cursos, experiencias, genero, edad)
