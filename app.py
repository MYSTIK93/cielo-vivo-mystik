import streamlit as st
from datetime import datetime, time

# Configuración visual de la marca MYSTIK
st.set_page_config(page_title="MYSTIK - El Cielo Vivo", page_icon="✨", layout="centered")

# Estilo personalizado con CSS (Colores: Negro, Dorado y Púrpura)
st.markdown("""
    <style>
    .main { background-color: #0d0d0d; color: #ffffff; }
    .stButton>button { background-color: #8e44ad; color: white; border-radius: 20px; border: 1px solid #f1c40f; width: 100%; font-weight: bold; }
    .stDateInput, .stTimeInput { background-color: #1a1a1a !important; }
    h1 { color: #f1c40f; text-align: center; font-family: 'serif'; }
    h3 { color: #d1d1d1; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌌 MYSTIK: Calculadora de Cielo Vivo")
st.write("---")

st.markdown("""
### El mapa del cielo no es estático.
Introduce tu **fecha y hora exacta** de nacimiento. Descubre dónde estaba el Sol realmente en el momento de tu primer aliento.
""")

# Entrada de datos
col1, col2 = st.columns(2)

with col1:
    fecha = st.date_input("Fecha de nacimiento", min_value=datetime(1920, 1, 1))

with col2:
    hora = st.time_input("Hora exacta (opcional)", value=time(12, 0))

# Lógica de Precisión (El Corazón de MYSTIK)
def calcular_posicion_exacta(dia, mes):
    if (mes == 4 and dia >= 19) or (mes == 5 and dia <= 13):
        return "Aries", "Vives en el impulso del fuego original. No eres la teoría, eres la acción."
    elif (mes == 5 and dia >= 14) or (mes == 6 and dia <= 21):
        return "Tauro", "La fuerza de la tierra bajo tus pies. Posees la belleza de lo tangible."
    elif (mes == 6 and dia >= 22) or (mes == 7 and dia <= 20):
        return "Géminis", "Mente de aire y palabras de luz. Eres el puente que une los mundos."
    elif (mes == 7 and dia >= 21) or (mes == 8 and dia <= 10):
        return "Cáncer", "Guardián de la memoria y la emoción. Tu caparazón protege un universo."
    elif (mes == 8 and dia >= 11) or (mes == 9 and dia <= 16):
        return "Leo", "El brillo soberano. Tu energía nace de la verdad, no del ego."
    elif (mes == 9 and dia >= 17) or (mes == 10 and dia <= 30):
        return "Virgo", "La alquimia del detalle. Encuentras la divinidad en la precisión."
    elif (mes == 10 and dia >= 31) or (mes == 11 and dia <= 23):
        return "Libra", "El equilibrio entre el caos y el orden. Eres la armonía en movimiento."
    elif (mes == 11 and dia >= 24) or (mes == 11 and dia <= 29):
        return "Escorpio", "Seis días de poder volcánico. Transformas todo lo que tocas."
    elif (mes == 11 and dia >= 30) or (mes == 12 and dia <= 17):
        return "Ophiuchus", "El Sanador Sagrado. Integras la serpiente y la luz. El signo trece es tu hogar."
    elif (mes == 12 and dia >= 18) or (mes == 1 and dia <= 20):
        return "Sagitario", "La flecha dirigida al infinito. Tu verdad no conoce fronteras."
    elif (mes == 12 and dia >= 21) or (mes == 2 and dia <= 16):
        return "Capricornio", "El arquitecto del tiempo. Construyes legados que desafían los siglos."
    elif (mes == 2 and dia >= 17) or (mes == 3 and dia <= 11):
        return "Acuario", "La vibración del futuro. Estás aquí para romper el viejo mapa."
    else:
        return "Piscis", "El océano de la consciencia. Eres el sueño que sueña el universo."

# Ejecución al presionar el botón
if st.button("CALCULAR MI VERDAD"):
    signo, mensaje = calcular_posicion_exacta(fecha.day, fecha.month)
    
    st.markdown(f"""
    <div style="border: 2px solid #f1c40f; padding: 20px; border-radius: 10px; text-align: center; background-color: #1a1a1a;">
        <h2 style="color: #f1c40f;">Tu Signo Real es {signo}</h2>
        <p style="font-style: italic; font-size: 18px; color: #ffffff;">"{mensaje}"</p>
        <p style="color: #d1d1d1;">A las {hora.strftime('%H:%M')} del {fecha.strftime('%d/%m/%Y')}, el cielo te marcó como un ser de {signo}.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.balloons()

# Footer con links
st.write("---")
st.markdown("📖 **[Descarga mi iBook en Apple Books](#)** | 🎙️ **[Escucha Cielo Vivo en Spotify](#)**")
st.write("🌌 **MYSTIK** | Sincronizando tu energía con el cielo real.")
