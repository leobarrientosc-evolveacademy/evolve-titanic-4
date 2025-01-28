import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Read the dataset
titanic = pd.read_csv("titanic.csv")

# Set up the dashboard title and description
st.set_page_config(layout="wide")
st.title("🚢 Dashboard de Análisis del Titanic")
st.write("Análisis interactivo de la demografía de pasajeros y factores de supervivencia en el Titanic")

# Sidebar filters
st.sidebar.header("Filtros")

# Age range filter
age_range = st.sidebar.slider(
    "Seleccionar Rango de Edad",
    int(titanic['Age'].min()),
    int(titanic['Age'].max()),
    (0, 80)
)

# Class filter
selected_classes = st.sidebar.multiselect(
    "Seleccionar Clases de Pasajeros",
    options=[1, 2, 3],
    default=[1, 2, 3],
    format_func=lambda x: f"{x}ra Clase"
)

# Gender filter
gender_map = {'male': 'Hombre', 'female': 'Mujer'}
selected_genders = st.sidebar.multiselect(
    "Seleccionar Género",
    options=titanic['Sex'].unique(),
    default=titanic['Sex'].unique(),
    format_func=lambda x: gender_map[x]
)

# Port filter
selected_ports = st.sidebar.multiselect(
    "Seleccionar Puerto de Embarque",
    options=titanic['Embarked'].dropna().unique(),
    default=titanic['Embarked'].dropna().unique(),
    format_func=lambda x: {'C': 'Cherburgo', 'Q': 'Queenstown', 'S': 'Southampton'}.get(x, x)
)

# Filter the dataset
filtered_data = titanic.copy()
filtered_data = filtered_data[
    (filtered_data['Age'].between(age_range[0], age_range[1])) &
    (filtered_data['Pclass'].isin(selected_classes)) &
    (filtered_data['Sex'].isin(selected_genders)) &
    (filtered_data['Embarked'].isin(selected_ports))
]

# Create two columns for the first row of visualizations
col1, col2 = st.columns(2)

with col1:
    # 1. Survival Rate by Class and Gender
    st.subheader("📊 Tasa de Supervivencia por Clase y Género")
    survival_stats = filtered_data.groupby(['Pclass', 'Sex'])['Survived'].agg(['count', 'mean']).reset_index()
    survival_stats['Tasa de Supervivencia'] = (survival_stats['mean'] * 100).round(2)
    survival_stats['Sex'] = survival_stats['Sex'].map(gender_map)
    fig1 = px.bar(survival_stats, 
                 x='Pclass', 
                 y='Tasa de Supervivencia',
                 color='Sex',
                 barmode='group',
                 labels={'Pclass': 'Clase de Pasajero', 'Sex': 'Género'},
                 title='Tasa de Supervivencia (%) por Clase y Género')
    fig1.update_layout(yaxis_title='Tasa de Supervivencia (%)')
    st.plotly_chart(fig1, use_container_width=True)
    st.write("""
    **¿Cómo se calcula?**
    - Se agrupa a los pasajeros por clase y género
    - Para cada grupo, se calcula el porcentaje de supervivientes
    - La tasa de supervivencia = (Número de sobrevivientes / Total de pasajeros del grupo) × 100
    """)

with col2:
    # 2. Age Distribution
    st.subheader("👥 Distribución de Edad por Supervivencia")
    fig2 = px.histogram(filtered_data,
                       x='Age',
                       color='Survived',
                       nbins=30,
                       labels={'Age': 'Edad', 'Survived': 'Sobrevivió', 'count': 'Cantidad'},
                       color_discrete_map={0: 'red', 1: 'green'},
                       title='Distribución de Edad por Estado de Supervivencia')
    fig2.update_layout(barmode='overlay', bargap=0.1)
    st.plotly_chart(fig2, use_container_width=True)
    st.write("""
    **¿Cómo se calcula?**
    - Se divide el rango de edades en 30 intervalos
    - Para cada intervalo, se cuenta el número de pasajeros
    - Color verde: sobrevivientes, Color rojo: no sobrevivientes
    - Las barras superpuestas permiten comparar la distribución de edades
    """)

# Create two columns for the second row
col3, col4 = st.columns(2)

with col3:
    # 3. Fare Distribution by Class
    st.subheader("💰 Distribución de Tarifas por Clase")
    fig3 = px.box(filtered_data,
                  x='Pclass',
                  y='Fare',
                  color='Survived',
                  labels={'Pclass': 'Clase', 'Fare': 'Tarifa', 'Survived': 'Sobrevivió'},
                  title='Distribución de Tarifas por Clase y Supervivencia')
    st.plotly_chart(fig3, use_container_width=True)
    st.write("""
    **¿Cómo se calcula?**
    - El diagrama de caja muestra la distribución de tarifas
    - La línea central es la mediana
    - La caja representa el 50% central de los datos
    - Los bigotes muestran los valores mínimos y máximos (excluyendo valores atípicos)
    - Los puntos son valores atípicos (tarifas inusualmente altas o bajas)
    """)

with col4:
    # 4. Family Size Impact
    st.subheader("👨‍👩‍👧‍👦 Impacto del Tamaño Familiar")
    filtered_data.loc[:, 'Tamaño Familiar'] = filtered_data['SibSp'] + filtered_data['Parch'] + 1
    family_survival = filtered_data.groupby('Tamaño Familiar')['Survived'].agg(['count', 'mean']).reset_index()
    family_survival['Tasa de Supervivencia'] = (family_survival['mean'] * 100).round(2)
    fig4 = px.line(family_survival[family_survival['count'] > 5],
                   x='Tamaño Familiar',
                   y='Tasa de Supervivencia',
                   markers=True,
                   title='Tasa de Supervivencia por Tamaño Familiar')
    st.plotly_chart(fig4, use_container_width=True)
    st.write("""
    **¿Cómo se calcula?**
    - Tamaño familiar = Número de hermanos/cónyuges + Número de padres/hijos + 1 (el pasajero)
    - Solo se muestran tamaños familiares con más de 5 casos
    - Tasa de supervivencia = (Sobrevivientes en cada tamaño familiar / Total de ese tamaño) × 100
    """)

# Create two columns for the third row
col5, col6 = st.columns(2)

with col5:
    # 5. Embarkation Port Analysis
    st.subheader("🚢 Análisis por Puerto de Embarque")
    port_survival = filtered_data.groupby('Embarked')['Survived'].mean().reset_index()
    port_survival['Tasa de Supervivencia'] = (port_survival['Survived'] * 100).round(2)
    fig5 = px.bar(port_survival,
                  x='Embarked',
                  y='Tasa de Supervivencia',
                  color='Embarked',
                  labels={'Embarked': 'Puerto de Embarque'},
                  title='Tasa de Supervivencia por Puerto de Embarque')
    fig5.update_xaxes(ticktext=['Cherburgo', 'Queenstown', 'Southampton'],
                      tickvals=['C', 'Q', 'S'])
    st.plotly_chart(fig5, use_container_width=True)
    st.write("""
    **¿Cómo se calcula?**
    - Se agrupa a los pasajeros por puerto de embarque
    - Para cada puerto, se calcula el porcentaje de supervivientes
    - C = Cherburgo, Q = Queenstown, S = Southampton
    - Tasa de supervivencia = (Sobrevivientes del puerto / Total de pasajeros del puerto) × 100
    """)

with col6:
    # 6. Cabin Deck Analysis
    st.subheader("🛳️ Análisis por Cubierta")
    filtered_data.loc[:, 'Cubierta'] = filtered_data['Cabin'].str[0].fillna('Desconocida')
    deck_survival = filtered_data.groupby('Cubierta')['Survived'].agg(['count', 'mean']).reset_index()
    deck_survival['Tasa de Supervivencia'] = (deck_survival['mean'] * 100).round(2)
    fig6 = px.bar(deck_survival[deck_survival['count'] > 5],
                  x='Cubierta',
                  y='Tasa de Supervivencia',
                  title='Tasa de Supervivencia por Cubierta')
    st.plotly_chart(fig6, use_container_width=True)
    st.write("""
    **¿Cómo se calcula?**
    - La cubierta se determina por la primera letra del número de cabina
    - Solo se muestran cubiertas con más de 5 pasajeros
    - 'Desconocida' indica cabinas sin información
    - Tasa de supervivencia = (Sobrevivientes de la cubierta / Total de pasajeros en la cubierta) × 100
    """)

# Create two columns for the fourth row
col7, col8 = st.columns(2)

with col7:
    # 7. Gender Distribution by Class
    st.subheader("⚖️ Distribución de Género por Clase")
    filtered_data['Género'] = filtered_data['Sex'].map(gender_map)
    class_gender = pd.crosstab(filtered_data['Pclass'], filtered_data['Género'], normalize='index') * 100
    fig7 = px.bar(class_gender,
                  barmode='stack',
                  labels={'Pclass': 'Clase', 'value': 'Porcentaje', 'Género': 'Género'},
                  title='Distribución de Género por Clase (%)')
    fig7.update_layout(yaxis_title='Porcentaje (%)')
    st.plotly_chart(fig7, use_container_width=True)
    st.write("""
    **¿Cómo se calcula?**
    - Se calcula la proporción de hombres y mujeres en cada clase
    - Las barras apiladas muestran la composición de género
    - El porcentaje total suma 100% para cada clase
    - Porcentaje = (Número de pasajeros de cada género / Total de pasajeros en la clase) × 100
    """)

with col8:
    # 8. Survival Rate by Title
    st.subheader("👑 Tasa de Supervivencia por Título")
    filtered_data.loc[:, 'Título'] = filtered_data['Name'].str.extract(r' ([A-Za-z]+)\.', expand=False)
    title_survival = filtered_data.groupby('Título')['Survived'].agg(['count', 'mean']).reset_index()
    title_survival['Tasa de Supervivencia'] = (title_survival['mean'] * 100).round(2)
    title_survival = title_survival[title_survival['count'] > 5].sort_values('Tasa de Supervivencia', ascending=False)
    fig8 = px.bar(title_survival,
                  x='Título',
                  y='Tasa de Supervivencia',
                  title='Tasa de Supervivencia por Título del Pasajero')
    st.plotly_chart(fig8, use_container_width=True)
    st.write("""
    **¿Cómo se calcula?**
    - Se extrae el título (Mr., Mrs., etc.) del nombre del pasajero
    - Solo se muestran títulos con más de 5 pasajeros
    - Se ordenan los títulos por tasa de supervivencia de mayor a menor
    - Tasa de supervivencia = (Sobrevivientes con el título / Total de pasajeros con el título) × 100
    """)

# Add summary statistics
st.header("📊 Estadísticas Resumen")
col_stats1, col_stats2, col_stats3, col_stats4 = st.columns(4)

with col_stats1:
    st.metric("Total de Pasajeros", len(filtered_data))
    
with col_stats2:
    survival_rate = (filtered_data['Survived'].mean() * 100).round(2)
    st.metric("Tasa de Supervivencia General", f"{survival_rate}%")
    
with col_stats3:
    avg_age = filtered_data['Age'].mean().round(2)
    st.metric("Edad Promedio", f"{avg_age} años")
    
with col_stats4:
    avg_fare = filtered_data['Fare'].mean().round(2)
    st.metric("Tarifa Promedio", f"£{avg_fare}")

# Add detailed insights
st.header("🔍 Hallazgos Clave")
st.write("""
1. **Impacto de Clase y Género**: 
   - Los pasajeros de primera clase tuvieron tasas de supervivencia significativamente más altas
   - Las mujeres tuvieron mayores tasas de supervivencia en todas las clases
   
2. **Patrones de Edad**: 
   - Los niños tuvieron mayores tasas de supervivencia
   - Los pasajeros de mediana edad fueron los más numerosos
   
3. **Efecto del Tamaño Familiar**:
   - Los pasajeros que viajaban con familias pequeñas (2-4 miembros) tuvieron mejores posibilidades de supervivencia
   - Las familias muy grandes tuvieron tasas de supervivencia más bajas
   
4. **Puerto de Embarque**:
   - Los pasajeros de Cherburgo tuvieron la tasa de supervivencia más alta
   - Southampton tuvo la mayor cantidad de pasajeros
   
5. **Ubicación de Cabina**:
   - Las cabinas en cubiertas superiores (A, B, C) mostraron mayores tasas de supervivencia
   - La información de cabina de muchos pasajeros es desconocida

*Nota: Este análisis se basa en el conjunto de datos filtrado actualmente. Ajustar los filtros actualizará todas las visualizaciones y estadísticas.*
""")
