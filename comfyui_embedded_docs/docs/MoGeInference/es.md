# Inferencia MoGe

Ejecute MoGe en una sola imagen para estimar profundidad y geometría. Este nodo procesa una imagen de entrada a través del modelo MoGe para generar una nube de puntos 3D, un mapa de profundidad, los intrínsecos de la cámara, una máscara y las normales de superficie.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `moge_model` | El modelo MoGe que se utilizará para la inferencia. | MOGE_MODEL | Sí | N/A |
| `image` | La imagen de entrada para la estimación de profundidad y geometría. Solo se utilizan los primeros tres canales de color (RGB). | IMAGE | Sí | N/A |
| `resolution_level` | Controla la resolución de procesamiento. 0 es el más rápido, 9 proporciona el mayor detalle. (por defecto: 9) | INT | Sí | 0 a 9 |
| `fov_x_degrees` | (Avanzado) Campo de visión horizontal de la cámara de origen en grados. Establece la distancia focal utilizada para reproyectar el mapa de profundidad en 3D. Establézcalo en 0.0 para recuperar automáticamente el campo de visión a partir de los puntos predichos. (por defecto: 0.0) | FLOAT | Sí | 0.0 a 170.0 |
| `batch_size` | Imágenes por llamada de inferencia. Reduzca este valor si se queda sin memoria en un video largo o en un conjunto de imágenes. (por defecto: 4) | INT | Sí | 1 a 64 |
| `force_projection` | (Avanzado) Fuerza la proyección de los puntos predichos. (por defecto: True) | BOOLEAN | Sí | True/False |
| `apply_mask` | (Avanzado) Establece los píxeles enmascarados (cielo o no válidos) a infinito en las salidas de puntos y profundidad para que las herramientas de mallado puedan ignorarlos. Desactívelo para mantener la geometría predicha sin procesar en todas partes; la máscara aún se devuelve por separado. (por defecto: True) | BOOLEAN | Sí | True/False |

Nota: Cuando la `image` de entrada contiene más fotogramas que `batch_size`, el nodo los procesa en múltiples llamadas de inferencia y combina los resultados en una única geometría de salida.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `moge_geometry` | Un diccionario que contiene la geometría estimada. Incluye la `image` original y puede contener `points` (nube de puntos 3D), `depth` (mapa de profundidad), `intrinsics` (matriz de intrínsecos de la cámara), `mask` (máscara que identifica píxeles válidos) y `normal` (normales de superficie). | MOGE_GEOMETRY |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeInference/es.md)

---
**Source fingerprint (SHA-256):** `59f6b8b1ab65147a47f5dc7ebee7b965a5ab37c6a0843a2c80d50c767ad98db4`
