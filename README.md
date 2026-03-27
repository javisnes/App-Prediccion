# 🌐 Aplicación Web: Predicción de Abandono de Clientes (Churn)

🔴 **[¡Prueba la aplicación interactiva en vivo aquí!](https://app-prediccion-lgqk5xvt78xvfvnj3xl4bv.streamlit.app/)**

## 🎯 Sobre el Proyecto
Este proyecto lleva un modelo de **Machine Learning** desde un entorno de desarrollo (Jupyter/Colab) a la vida real. Se construyó una aplicación web interactiva que permite a cualquier usuario del área de negocio (sin conocimientos de programación) predecir si un cliente va a cancelar su servicio.

## ✨ Características Principales
* **Interfaz Intuitiva:** Controles deslizables y menús desplegables para ingresar el perfil del cliente en segundos.
* **Predicción en Tiempo Real:** El motor de Machine Learning procesa los datos instantáneamente y devuelve un diagnóstico.
* **Recomendaciones de Negocio:** La IA no solo da un porcentaje, sino que sugiere acciones inmediatas (ej. ofrecer descuentos o intentar *upselling*).

## 🛠️ Tecnologías Utilizadas
* **Streamlit:** Desarrollo de la interfaz web (Front-end) y despliegue del servidor.
* **Scikit-Learn:** Algoritmo de clasificación `RandomForestClassifier`.
* **Pandas:** Estructuración y manipulación de los datos ingresados por el usuario.

## 💻 ¿Cómo correrlo localmente?
Si eres desarrollador y quieres correr esta aplicación en tu propia computadora, sigue estos pasos:

1. Clona este repositorio.
2. Instala las dependencias ejecutando: `pip install -r requirements.txt`
3. Inicia el servidor local de Streamlit ejecutando: `streamlit run app.py`

---
*Desarrollado para transformar datos complejos en soluciones de negocio accesibles.*
