# Tripo: Modelo de textura

El nodo TripoTextureNode genera modelos 3D con texturas utilizando la API de Tripo. Toma un ID de tarea de modelo y aplica la generación de texturas con varias opciones, incluyendo materiales PBR, ajustes de calidad de textura y métodos de alineación. El nodo se comunica con la API de Tripo para procesar la solicitud de generación de texturas y devuelve el archivo de modelo resultante y el ID de tarea.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `id_de_tarea_del_modelo` | El ID de la tarea del modelo al que se le aplicarán texturas | MODEL_TASK_ID | Sí | - |
| `textura` | Si se generan texturas (por defecto: True) | BOOLEAN | No | - |
| `pbr` | Si se generan materiales PBR (renderizado basado en la física) (por defecto: True) | BOOLEAN | No | - |
| `semilla_de_textura` | Semilla aleatoria para la generación de texturas (por defecto: 42) | INT | No | - |
| `calidad_de_textura` | Nivel de calidad para la generación de texturas (por defecto: "standard"). La opción "detailed" cuesta $0.20 USD, mientras que "standard" cuesta $0.10 USD. | COMBO | No | "standard"<br>"detailed" |
| `alineación_de_textura` | Método para alinear texturas (por defecto: "original_image"). "original_image" alinea las texturas con la imagen de entrada original, mientras que "geometry" las alinea con la geometría 3D. | COMBO | No | "original_image"<br>"geometry" |
| `texture_prompt` | Guía de texto opcional para el texturizado. En la práctica, es necesaria para modelos importados (Tripo: Import Model), que no tienen una imagen de origen de la que inferir colores. (por defecto: "") | STRING | No | - |

*Nota: Este nodo requiere tokens de autenticación y claves de API que el sistema maneja automáticamente.*

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `archivo_de_modelo` | El archivo de modelo generado con las texturas aplicadas (solo por compatibilidad con versiones anteriores) | STRING |
| `id_de_tarea_de_modelo` | El ID de tarea para el seguimiento del proceso de generación de texturas | MODEL_TASK_ID |
| `GLB` | El modelo 3D generado en formato GLB con las texturas aplicadas | FILE3DGLB |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/es.md)

---
**Source fingerprint (SHA-256):** `a0157b7fa2bb94d174ea5893d7389885180876794032a510642586e310ba30d4`
