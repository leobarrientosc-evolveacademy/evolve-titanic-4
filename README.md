## TITANIC ##

### Análisis de Supervivientes del Titanic con Streamlit

# 2. Introducción

### Breve resumen:

El Titanic fue un transatlántico que se hundió en 1912. Su trágico destino lo ha convertido en un símbolo de desastre y, a la vez, en un rico conjunto de datos para análisis. ¿Por qué? Porque ofrece una gran cantidad de información sobre las personas a bordo (edad, sexo, clase social, etc.) y una pregunta clara: ¿quién sobrevivió y por qué? Esta combinación lo hace ideal para aplicar técnicas de aprendizaje automático y estadística.

Objetivo del proyecto: Lo que se pretende es poder analizar las causas de que hubiera tantos desaparecidos y cuales son las medidas a tomar para mejorar.

Alcance del proyecto: Lo que se va a realizar en primer lugar es un análisis de la edad, sexo y situación del camarote.
## Objetivo del proyecto:

El objetivo principal es identificar los factores que influyeron en la supervivencia de los pasajeros. Es decir, queremos responder preguntas como:

- ¿La clase social influyó en las posibilidades de sobrevivir?
- ¿El género fue un factor determinante?
- ¿La edad jugó un papel importante?
- ¿Otros factores como el número de familiares a bordo o el lugar de embarque influyeron?

### Alcance del proyecto:

Este análisis se centrará en las variables más relevantes relacionadas con los pasajeros y su supervivencia. Utilizaremos técnicas de visualización de datos y modelos de machine learning para identificar patrones y correlaciones. Las técnicas específicas que se emplearán incluyen:


- Análisis exploratorio de datos (EDA): Para comprender la distribución de las variables y detectar valores atípicos.
- Visualizaciones: Histogramas, gráficos de barras, diagramas de dispersión y heatmaps para representar los datos de forma clara y concisa.
- Modelado predictivo: Utilizaremos algoritmos de clasificación como la regresión logística para construir un modelo que prediga la probabilidad de supervivencia en función de las características de un pasajero.

### Técnicas utilizadas:

- Visualización de datos: Histogramas, diagramas de caja, gráficos de barras, etc.
- Estadística descriptiva: Medidas de tendencia central (media, mediana) y dispersión (desviación estándar).
- Aprendizaje automático: Algoritmos de clasificación supervisada.
  Evaluación de modelos: Matrices de confusión, curvas ROC, etc.

# 3. Datos Utilizados

### Fuente de los datos:

El conjunto de datos utilizado en este proyecto se obtuvo de Kaggle, una popular plataforma de ciencia de datos.


### Descripción general del dataset:

El dataset del Titanic contiene aproximadamente [número] filas (pasajeros) y [número] columnas (variables). Las principales variables incluyen:

Survived: Indica si el pasajero sobrevivió (1) o no (0).
Pclass: Clase del billete (1 = Primera, 2 = Segunda, 3 = Tercera).
Sex: Sexo del pasajero.
Age: Edad del pasajero.
SibSp: Número de hermanos/cónyuges a bordo.
Parch: Número de padres/hijos a bordo.   
Fare: Tarifa del pasaje.
Embarked: Puerto de embarque (C = Cherbourg, Q = Queenstown, S = Southampton).

### Limpieza y preprocesamiento:

Antes de realizar el análisis, se llevaron a cabo las siguientes tareas de limpieza y preprocesamiento:

Manejo de valores faltantes: Se imputaron los valores faltantes de la edad utilizando la mediana.
Codificación de variables categóricas: Se convirtieron las variables categóricas (como el sexo y el puerto de embarque) en variables numéricas utilizando técnicas de one-hot encoding.
Creación de nuevas variables: Se crearon nuevas variables, como la edad en grupos, para explorar relaciones más profundas.

# 4. Funcionalidades de la Aplicación

### Visualizaciones:

La aplicación de Streamlit incluirá una variedad de visualizaciones interactivas, como:

Histogramas: Para mostrar la distribución de variables numéricas como la edad y la tarifa.
Gráficos de barras: Para comparar la proporción de supervivientes entre diferentes grupos (por ejemplo, por clase o sexo).
Diagramas de dispersión: Para explorar la relación entre variables numéricas.
Heatmaps: Para visualizar la correlación entre variables.

### Interactividad:

Los usuarios podrán interactuar con la aplicación de las siguientes maneras:

Filtros: Seleccionar un rango de edades, una clase específica o un género para analizar subconjuntos de datos.
Selectores: Elegir diferentes variables para comparar o visualizar.
Tooltips: Obtener información detallada al pasar el cursor sobre los elementos de los gráficos.

### Análisis clave:

Los hallazgos clave del análisis incluirán:

Importancia de la clase social: Los pasajeros de primera clase tuvieron una mayor probabilidad de supervivencia.
Impacto del género: Las mujeres y los niños tuvieron una mayor tasa de supervivencia en comparación con los hombres.
Efecto de la edad: Los niños muy pequeños y los adultos jóvenes tuvieron una mayor probabilidad de sobrevivir.
Influencia del puerto de embarque: El puerto de embarque podría haber tenido un impacto en la supervivencia debido a la ubicación de los botes salvavidas.
