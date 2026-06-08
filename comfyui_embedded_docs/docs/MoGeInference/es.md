# Descripción general

Ejecuta MoGe en una sola imagen para estimar profundidad y geometría. Este nodo procesa una imagen de entrada a través del modelo MoGe para generar una nube de puntos 3D, un mapa de profundidad, los parámetros intrínsecos de la cámara, una máscara y normales de superficie.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `moge_model` | El modelo MoGe a utilizar para la inferencia. | MOGE_MODEL | Sí | N/D |
| `image` | La imagen de entrada para la estimación de profundidad y geometría. | IMAGE | Sí | N/D |
| `resolution_level` | Controla la resolución de procesamiento. 0 es el más rápido, 9 proporciona el mayor detalle. (valor predeterminado: 9) | INT | Sí | 0 a 9 |
| `fov_x_degrees` | Campo de visión horizontal de la cámara fuente en grados. Establece la distancia focal utilizada para reproyectar el mapa de profundidad a 3D. Establézcalo en 0.0 para recuperar automáticamente el campo de visión a partir de los puntos predichos. (valor predeterminado: 0.0) | FLOAT | Sí | 0.0 a 170.0 |
| `batch_size` | Número de imágenes procesadas por llamada de inferencia. Reduzca este valor si se queda sin memoria al procesar videos largos o conjuntos grandes de imágenes. (valor predeterminado: 4) | INT | Sí | 1 a 64 |
| `force_projection` | (Avanzado) Fuerza la proyección de los puntos predichos. (valor predeterminado: Verdadero) | BOOLEAN | Sí | Verdadero/Falso |
| `apply_mask` | Cuando está habilitado, establece los píxeles enmascarados (cielo o inválidos) como infinito en las salidas de puntos y profundidad. Esto ayuda a las herramientas de mallado a ignorar estas áreas. Deshabilítelo para mantener la geometría predicha sin procesar en todas partes; la máscara aún se devuelve por separado. (valor predeterminado: Verdadero) | BOOLEAN | Sí | Verdadero/Falso |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `moge_geometry` | Un diccionario que contiene la geometría estimada. Incluye la `image` original, y puede contener `points` (nube de puntos 3D), `depth` (mapa de profundidad), `intrinsics` (matriz de parámetros intrínsecos de la cámara), `mask` (máscara que identifica píxeles válidos) y `normal` (normales de superficie). | MOGE_GEOMETRY |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeInference/es.md)

---
**Source fingerprint (SHA-256):** `5213b280513850eeef2e22ae723ebb015789109435e28ddd79f91f9a4b4a1e79`
