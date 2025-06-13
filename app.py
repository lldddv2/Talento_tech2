import streamlit as st
from PIL import Image # Pillow para manejar imágenes PNG
import os # Para manejar rutas de archivos

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Dashboard de Datos Urbanos",
    page_icon="🏙️",
    layout="wide", # Usa el ancho completo de la pantalla
    initial_sidebar_state="expanded"
)

# --- FUNCIÓN PARA CONSTRUIR LA RUTA DE LA IMAGEN ---
# Esta función es crucial para que Streamlit encuentre tus imágenes
def get_image_path(image_name):
    # Obtiene la ruta del directorio actual del script (donde está app.py)
    script_dir = os.path.dirname(__file__)
    # Construye la ruta completa a la imagen dentro de la carpeta 'images'
    image_path = os.path.join(script_dir, "images", image_name)
    return image_path

# --- BARRA LATERAL ---
with st.sidebar:
    st.title("🏙️ Navegación")
    st.markdown("---")

    # Selector de página/sección
    page_selection = st.radio(
        "Selecciona una sección:",
        ["🌬️ Calidad del Aire (PM2.5)", "🚇 Uso del Metro", "ℹ️ Acerca de"]
    )

    st.markdown("---")
    st.write("Desarrollado con en Streamlit")

# --- CONTENIDO PRINCIPAL ---

if page_selection == "🌬️ Calidad del Aire (PM2.5)":
    st.title("🌬️ Análisis de Calidad del Aire (PM2.5)")
    st.write("Explora los datos históricos y animaciones de la concentración de partículas PM2.5 en diferentes zonas.")

    st.markdown("---")

    # Sección para la Zona CA
    st.header("📍 Zona CA")
    st.markdown("### Datos de PM2.5 para la Zona CA")

    col_ca_hist, col_ca_anim = st.columns(2)

    with col_ca_hist:
        st.subheader("Mapa Histórico de PM2.5 (CA)")
        image_path_cah_pm25 = get_image_path("CAH_PM25.png")
        if os.path.exists(image_path_cah_pm25):
            st.image(image_path_cah_pm25, caption="Concentración Histórica de PM2.5 en la Zona CA", use_container_width=True)
            st.markdown("Ciclo diurno de usuarios que toman el Metro de Medellín como forma de transporte. La línea negra corresponde al promedio, mientras que el área gris corresponde al rango de variación definido a partir de más o menos una desviación estándar.")
        else:
            st.warning(f"Imagen no encontrada: {image_path_cah_pm25}")

    with col_ca_anim:
        st.subheader("Animación de Evolución de PM2.5 (CA)")
        # Para GIFs, Streamlit necesita la ruta directa o bytes.
        # get_image_path() ya devuelve la ruta, así que la usamos directamente.
        gif_path_ca_animacion = get_image_path("CA_PM25_animacion.gif")
        if os.path.exists(gif_path_ca_animacion):
            st.image(gif_path_ca_animacion, caption="Evolución Temporal de PM2.5 en la Zona CA", use_container_width=True)
            st.markdown("Esta animación visualiza cómo han variado las concentraciones de PM2.5 en la Zona CA a lo largo del tiempo.")
        else:
            st.warning(f"GIF no encontrado: {gif_path_ca_animacion}")

    st.markdown("---")

    # Sección para la Zona CD
    st.header("📍 Zona CD")
    st.markdown("### Datos de PM2.5 para la Zona CD")

    col_cd_hist, col_cd_anim = st.columns(2)

    with col_cd_hist:
        st.subheader("Mapa Histórico de PM2.5 (CD)")
        image_path_cdh_pm25 = get_image_path("CDH_PM25.png")
        if os.path.exists(image_path_cdh_pm25):
            st.image(image_path_cdh_pm25, caption="Concentración Histórica de PM2.5 en la Zona CD", use_container_width=True)
            st.markdown("Ciclo diurno del material particulado PM2.5. La línea negra sólida corresponde al promedio de toda la red de ciudadanos científicos, mientras que las líneas grises corresponden a cada uno de los sensores de bajo costo que conforman la red de ciudadanos científicos.")
        else:
            st.warning(f"Imagen no encontrada: {image_path_cdh_pm25}")

    with col_cd_anim:
        st.subheader("Animación de Evolución de PM2.5 (CD)")
        gif_path_cd_animacion = get_image_path("CD_PM25_animacion.gif")
        if os.path.exists(gif_path_cd_animacion):
            st.image(gif_path_cd_animacion, caption="Evolución Temporal de PM2.5 en la Zona CD", use_container_width=True)
            st.markdown("Observa la variación de las concentraciones de PM2.5 en la Zona CD a lo largo del tiempo a través de esta animación.")
        else:
            st.warning(f"GIF no encontrado: {gif_path_cd_animacion}")


elif page_selection == "🚇 Uso del Metro":
    st.title("🚇 Análisis de Uso del Metro")
    st.write("Visualización de los patrones de uso del sistema de transporte Metro.")

    st.markdown("---")

    col_cd_1, col_cd_2 = st.columns(2)

    with col_cd_1:
        st.subheader("Ciclo diurno de Usuarios del Metro")
        image_path_cdh_metro_users = get_image_path("CDH_Metro_users.png")
        if os.path.exists(image_path_cdh_metro_users):
            st.image(image_path_cdh_metro_users, caption="Gráfico de Usuarios del Metro en la Zona CD", use_container_width=True)
            st.markdown("""
                Ciclo diurno de usuarios que toman el Metro de Medellín como forma de transporte. La línea negra corresponde al promedio, mientras que el área gris corresponde al rango de variación definido a partir de más o menos una desviación estándar.
            """)
        else:
            st.warning(f"Imagen no encontrada: {image_path_cdh_metro_users}")
    
    with col_cd_2:
        st.subheader("Ciclo anual de usuarios del Metro")
        image_path_cdh_metro_users_hist = get_image_path("CAH_metro_users.png")
        if os.path.exists(image_path_cdh_metro_users_hist):
            st.image(image_path_cdh_metro_users_hist, caption="Histograma de Usuarios del Metro en la Zona CD", use_container_width=True)
            st.markdown("""
                Ciclo anual de usuarios que toman el Metro de Medellín como forma de transporte. La línea negra sólida corresponde al promedio total, mientras que la línea verde corresponde al promedio removiendo los años de pandemia. Finalmente, las áreas grises y verdes corresponden al rango de variabilidad definido a partir de más o menos una desviación estándar.
            """)
        else:
            st.warning(f"Imagen no encontrada: {image_path_cdh_metro_users_hist}")


elif page_selection == "ℹ️ Acerca de":
    st.title("ℹ️ Acerca de este Dashboard")
    st.write("Este dashboard ha sido creado para visualizar y explorar datos clave relacionados con la calidad del aire y el uso del transporte público en áreas urbanas.")

    st.subheader("Fuentes de Datos")
    st.write("""
    *   **Calidad del Aire (PM2.5):** Datos históricos de sensores de calidad del aire.
    *   **Uso del Metro:** Registros de afluencia de pasajeros del sistema de transporte Metro.
    """)

    st.subheader("Tecnologías Utilizadas")
    st.markdown("""
    *   **Streamlit:** Para la construcción interactiva del dashboard.
    *   **Python:** Lenguaje de programación.
    *   **Pillow (PIL):** Librería para el procesamiento de imágenes.
    *   **Librerías de visualización (ej: Matplotlib, Seaborn):**
    """)

    st.subheader("Desarrolladores")
    st.write("""
    *   Alexis Ayala
    *   Sara Carvajal
    *   Juan Manuel Herrera
    *   Luis Díaz 
""")
    st.write("Contacto: [s.carvajal@udea.edu.co](mailto:s.carvajal@udea.edu.co)")
    st.markdown("---")
    st.write("Fecha de Creación: 2025-06-11")