> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeInference/es.md)

# Descripción general

Ejecuta MoGe en una sola imagen para estimar profundidad y geometría. Este nodo procesa una imagen de entrada a través del modelo MoGe para generar una nube de puntos 3D, un mapa de profundidad, los parámetros intrínsecos de la cámara, una máscara y normales de superficie.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `moge_model` | MOGE_MODEL | Sí | N/D | El modelo MoGe a utilizar para la inferencia. |
| `image` | IMAGE | Sí | N/D | La imagen de entrada para la estimación de profundidad y geometría. |
| `resolution_level` | INT | Sí | 0 a 9 | Controla la resolución de procesamiento. 0 es el más rápido, 9 proporciona el mayor detalle. (valor predeterminado: 9) |
| `fov_x_degrees` | FLOAT | Sí | 0.0 a 170.0 | Campo de visión horizontal de la cámara fuente en grados. Establece la distancia focal utilizada para reproyectar el mapa de profundidad a 3D. Establézcalo en 0.0 para recuperar automáticamente el campo de visión a partir de los puntos predichos. (valor predeterminado: 0.0) |
| `batch_size` | INT | Sí | 1 a 64 | Número de imágenes procesadas por llamada de inferencia. Reduzca este valor si se queda sin memoria al procesar videos largos o conjuntos grandes de imágenes. (valor predeterminado: 4) |
| `force_projection` | BOOLEAN | Sí | Verdadero/Falso | (Avanzado) Fuerza la proyección de los puntos predichos. (valor predeterminado: Verdadero) |
| `apply_mask` | BOOLEAN | Sí | Verdadero/Falso | Cuando está habilitado, establece los píxeles enmascarados (cielo o inválidos) como infinito en las salidas de puntos y profundidad. Esto ayuda a las herramientas de mallado a ignorar estas áreas. Deshabilítelo para mantener la geometría predicha sin procesar en todas partes; la máscara aún se devuelve por separado. (valor predeterminado: Verdadero) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `moge_geometry` | MOGE_GEOMETRY | Un diccionario que contiene la geometría estimada. Incluye la `image` original, y puede contener `points` (nube de puntos 3D), `depth` (mapa de profundidad), `intrinsics` (matriz de parámetros intrínsecos de la cámara), `mask` (máscara que identifica píxeles válidos) y `normal` (normales de superficie). |

---
**Source fingerprint (SHA-256):** `5213b280513850eeef2e22ae723ebb015789109435e28ddd79f91f9a4b4a1e79`
