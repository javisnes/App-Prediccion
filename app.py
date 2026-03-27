import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# --- 1. CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Predictor de Churn", page_icon="📉", layout="centered")

st.title("🤖 Predictor de Abandono de Clientes")
st.markdown("Esta aplicación web utiliza **Machine Learning (Random Forest)** para predecir si un cliente cancelará su servicio de telecomunicaciones basándose en su perfil.")

# --- 2. ENTRENAMIENTO DEL MODELO (Oculto al usuario) ---
# Usamos cache para que la IA solo se entrene una vez cuando se abre la página
@st.cache_resource
def cargar_modelo():
    # Generamos datos simulados rápidos (Mismo pipeline que tu Colab)
    data = {
        'Edad': [25, 45, 30, 60, 22, 55, 35, 70, 40, 50] * 10,
        'Cargos_Mensuales': [20.5, 80.0, 45.5, 105.0, 25.0, 95.0, 55.0, 115.0, 65.0, 85.0] * 10,
        'Meses_Antiguedad': [2, 48, 12, 60, 1, 36, 24, 72, 6, 18] * 10,
        'Tipo_Contrato': ['Mensual', 'Anual', 'Mensual', 'Anual', 'Mensual', 'Anual', 'Mensual', 'Anual', 'Mensual', 'Anual'] * 10,
        'Abandono': ['Si', 'No', 'Si', 'No', 'Si', 'No', 'No', 'No', 'Si', 'No'] * 10
    }
    df = pd.DataFrame(data)
    
    le_contrato = LabelEncoder()
    df['Tipo_Contrato_Num'] = le_contrato.fit_transform(df['Tipo_Contrato'])
    
    X = df[['Edad', 'Cargos_Mensuales', 'Meses_Antiguedad', 'Tipo_Contrato_Num']]
    y = df['Abandono']
    
    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    modelo.fit(X, y)
    
    return modelo, le_contrato

modelo, le_contrato = cargar_modelo()

# --- 3. INTERFAZ DE USUARIO (Panel Lateral) ---
st.sidebar.header("⚙️ Ingresa los datos del cliente")

# Controles interactivos
edad = st.sidebar.slider("Edad del cliente", 18, 90, 35)
cargos = st.sidebar.slider("Cargos Mensuales ($)", 10.0, 150.0, 60.0)
meses = st.sidebar.slider("Meses de Antigüedad", 0, 72, 12)
contrato = st.sidebar.selectbox("Tipo de Contrato", ['Mensual', 'Anual'])

# --- 4. PROCESAMIENTO Y PREDICCIÓN ---
st.write("---")
st.subheader("🔍 Resultados del Análisis")

# Botón para activar la predicción
if st.button("Calcular Riesgo de Abandono"):
    # Convertir el texto del contrato al número que entiende la IA
    contrato_num = le_contrato.transform([contrato])[0]
    
    # Crear la tabla con el cliente nuevo
    cliente_nuevo = pd.DataFrame([[edad, cargos, meses, contrato_num]], 
                                 columns=['Edad', 'Cargos_Mensuales', 'Meses_Antiguedad', 'Tipo_Contrato_Num'])
    
    # Hacer la predicción
    prediccion = modelo.predict(cliente_nuevo)[0]
    probabilidad = modelo.predict_proba(cliente_nuevo)[0] # Qué tan segura está la IA
    
    # Mostrar resultados con diseño
    st.write(f"**Perfil analizado:** Cliente de {edad} años, con contrato {contrato}, pagando ${cargos} desde hace {meses} meses.")
    
    if prediccion == 'Si':
        st.error(f"⚠️ **ALTO RIESGO DE ABANDONO**")
        st.write(f"La Inteligencia Artificial estima un **{probabilidad[1]*100:.1f}%** de probabilidad de que el cliente cancele el servicio.")
        st.info("💡 **Recomendación:** Ofrecer un descuento inmediato o intentar migrar a un contrato Anual.")
    else:
        st.success(f"✅ **CLIENTE SEGURO**")
        st.write(f"La Inteligencia Artificial estima un **{probabilidad[0]*100:.1f}%** de probabilidad de retención.")
        st.info("💡 **Recomendación:** Cliente estable. Excelente candidato para ofrecer servicios adicionales (Upselling).")

st.caption("Desarrollado por Javier - Analista de Datos")
