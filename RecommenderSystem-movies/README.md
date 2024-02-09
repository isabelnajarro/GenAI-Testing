# MovIA
El MovIA Recommender System cuenta con 3 posibilidades: buscar una película según tu estado de ánimo, buscar una película según tu perfil de usuario y buscar una película según una descripción que comentes.

## Descripción
### Opción 1: Buscar una película según tu estado de ánimo
Este método (recommend_movie_by_mood) recomienda una película al usuario basándose en su estado de ánimo actual. Primero, solicita al usuario información sobre su estado de ánimo y preferencias de género mediante la función welcome_feeling(). Luego, utiliza esta información para obtener recomendaciones de películas mediante el método get_recommendations(). Si se encuentran películas recomendadas, imprime el título de la primera película recomendada y llama al método process_recommendation() para continuar con el proceso de recomendación.
Esta busqueda se hace ya que nos encontramos con una base de datos en Astra para la que llamamos al método search_film() que busca películas basadas en un texto proporcionado. Utiliza el texto como prompt para buscar películas mediante el método search_vector().

### Opción 2: Buscar una película según tu perfil de usuario
Esta opción (recommend_movie_based_on_profile()) permite al usuario buscar una película basada en su perfil personal registrado en la aplicación. Este método se encarga de recomendar una película basada en las preferencias de género del usuario registrado.
Comprueba si hay un usuario activo y obtiene las preferencias de género del usuario y busca películas que coincidan con las preferencias del usuario en la base de datos de Astra.

### Opcion 3: Buscar una película según una descripcion dada por el usuario
Esta opción (choose_movie_based_on_description) permite al usuario buscar una película especificando una descripción de lo que está buscando en la película. Primero, se le permite al usuario especificar una descripción de la película que está buscando.
Utiliza la descripción proporcionada por el usuario para generar una recomendación de película utilizando el modelo de OpenAI y se buscan películas que coincidan con la descripción proporcionada.

### Manejo de la respuesta del usuario
Existen unos métodos en el código que se encargan de gestionar la respuesta del usuario en cuanto a si le gusta la selección de películas. Si hay películas disponibles en self.films, solicitan la opinión del usuario y llaman a otros métodos para procesar su respuesta. Luego, se imprime un mensaje de confirmación junto con el título de la película recomendada, en caso de que haya una.

## Preprocesamiento de los datos

## Librerías involucradas
```bash
pip install pandas
pip install nltk
pip install spacy
pip install transformers
pip install astrapy
pip install langchain-openai
pip install python-dotenv
```
## Ejecución

```bash
python3 RecommenderSystem.py
```

## Pruebas de uso
