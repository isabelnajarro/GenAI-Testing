# MovIA
El MovIA Recommender System cuenta con 3 posibilidades: buscar una película según tu estado de ánimo, buscar una película según tu perfil de usuario y buscar una película según una descripción que comentes.

## Preprocesamiento de los datos
Los datos del dataset [The Movies Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset) se han preprocesado para poder trabajar con ellos posteriormente en el recomendador.
- Preprocess movies.ipynb: Primer procesamiento donde se establece el formato de las variables con las que contamos y se limpian los datos de nulos.
- Bert-LanguagesToEnglish.ipynb: Al observar como estaban los datos, se hizo necesario preprocesar los idiomas de las películas para poder contar con todos los idiomas en inglés, esto se hace mediante el uso de la librería OpenAI.
- NLTK-GetKeyWordsFromOverview.ipynb: Tras esto pasamos a rellenar los keywords faltantes con procesamiento del lenguaje natural de la descripción. Se escogen 3 palabras que describan la descripción.
- GPT-PredicciónGenerosPorDescripcion.ipynb: con ayuda de gp2 (es el modelo que me ha dejado usar el código sin problemas) se generan los géneros de las películas a partir de su descripción.
- DataStax_UploadFilms.ipynb: sube el contenido del csv final a una base de datos de Astra.

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

## Pruebas incompletas
- Se ha generado en la carpeta de preprocesamiento un fichero ColumnRecommendedAge.ipynb que lee la descripción de las películas y consigue sacar cual es la edad recomendada para visualizarla. Este código funciona bien pero su tardanza (procesa película por segundo y trabajamos con 5000 y era mucho tiempo de espera) nos han llevado a descartarlo del código final.
- LangChain: también se ha intentado utilizar la librería langchain para la tercera opción pero problemas con la librería han derivado a usar finalmente OpenAI.

## Posibles ampliaciones
- Añadir generos para emociones positivas y negativas para el usuario. Con esta ampliación podemos orientar más la recomendación y tener más posibilidad de acierto. Ejemplo: Si una persona cuando se encuentra triste le gustan más los dramas que las comedias que le ofrezca el género que más le gusta sobre el resto.
- Añadir lastRecommendation en el usuario. Con esta ampliación podemos saber qué película fue la última recomendada y poder preguntarle por la nota y poder hacer un diccionario que almacene la película y la nota que obtuvo para ayudar al recomendador en el futuro ya que si la nota obtenida es parecida a la nota media de la pelicula es una manera de decirle al recomendador que va bien y establecer reglas para las siguientes recomendaciones.

## Descripción
### Opción 1: Buscar una película según tu estado de ánimo
Este método (recommend_movie_by_mood) recomienda una película al usuario basándose en su estado de ánimo actual. Primero, solicita al usuario información sobre su estado de ánimo y preferencias de género mediante la función welcome_feeling(). Luego, utiliza esta información para obtener recomendaciones de películas mediante el método get_recommendations(). Si se encuentran películas recomendadas, imprime el título de la primera película recomendada y llama al método process_recommendation() para continuar con el proceso de recomendación.
Al empezar la ejecución existe un método getPositiveAndNegativeGenres() que genera 2 listas de géneros considerados positivos y negativos por si el usuario no quiere indicar ningún género. 
Esta busqueda se hace ya que nos encontramos con una base de datos en Astra para la que llamamos al método search_film() que busca películas basadas en un texto proporcionado. Utiliza el texto como prompt para buscar películas mediante el método search_vector().

### Opción 2: Buscar una película según tu perfil de usuario
Esta opción (recommend_movie_based_on_profile()) permite al usuario buscar una película basada en su perfil personal registrado en la aplicación. Este método se encarga de recomendar una película basada en las preferencias de género del usuario registrado.
Comprueba si hay un usuario activo y obtiene las preferencias de género del usuario y busca películas que coincidan con las preferencias del usuario en la base de datos de Astra.

### Opcion 3: Buscar una película según una descripcion dada por el usuario
Esta opción (choose_movie_based_on_description) permite al usuario buscar una película especificando una descripción de lo que está buscando en la película. Primero, se le permite al usuario especificar una descripción de la película que está buscando.
Utiliza la descripción proporcionada por el usuario para generar una recomendación de película utilizando el modelo de OpenAI y se buscan películas que coincidan con la descripción proporcionada.

### Manejo de la respuesta del usuario
Existen unos métodos en el código que se encargan de gestionar la respuesta del usuario en cuanto a si le gusta la selección de películas. Si hay películas disponibles en self.films, solicitan la opinión del usuario y llaman a otros métodos para procesar su respuesta. Luego, se imprime un mensaje de confirmación junto con el título de la película recomendada, en caso de que haya una.
