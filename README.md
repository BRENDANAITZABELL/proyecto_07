🚗 Análisis de Vehículos Usados - Aplicación Web con Streamlit
Bienvenido a esta aplicación web interactiva desarrollada con Streamlit, que permite analizar datos de vehículos usados en EE. UU. de manera sencilla, visual y dinámica. Esta herramienta es ideal para usuarios interesados en explorar tendencias de precios, tipos de vehículos, kilometraje y más.

🧠 ¿Qué hace esta aplicación?
La aplicación toma como base el conjunto de datos vehicles_us.csv y ofrece funcionalidades interactivas para:

🔎 Explorar datos filtrados
Permite filtrar los vehículos por:

Año del modelo 📅 (rango personalizado entre 1990 y 2025)

Tipo de transmisión ⚙️ (manual, automática, etc.)

Tipo de vehículo 🚙 (SUV, sedán, pickup, etc.)

📊 Visualizar tablas y gráficos
Muestra información procesada en tablas y visualizaciones:

Tabla interactiva con los datos filtrados 📋

Precio promedio por modelo en un gráfico de barras 💵

Kilometraje promedio por año del modelo en un gráfico de dispersión 🚦

🔧 Funcionalidades
🎛️ Barra lateral de filtros para ajustar los criterios de análisis.

📈 Gráficos dinámicos con Plotly para una mejor interpretación visual.

✅ Botón para aplicar todos los filtros y actualizar los resultados.

🗂️ Tablas con datos agrupados para facilitar el análisis de tendencias.

🚀 ¿Cómo ejecutarla?
Asegúrate de tener Python y las siguientes bibliotecas instaladas:

nginx
Copiar
Editar
pip install pandas plotly streamlit
Ejecuta la aplicación con:

arduino
Copiar
Editar
streamlit run app.py
Se abrirá en tu navegador por defecto una interfaz interactiva.

📁 Archivos
app.py → Código principal de la aplicación.

vehicles_us.csv → Conjunto de datos con información de vehículos usados.

💡 Objetivo del Proyecto
Este proyecto fue desarrollado como parte de un ejercicio práctico para aprender sobre visualización de datos, filtros dinámicos y desarrollo de aplicaciones web simples con Python. Ideal para tomar decisiones basadas en datos dentro del mercado automotriz.

