# Inferencia MoGe

Ejecuta MoGe en una sola imagen para estimar profundidad y geometría. Este nodo procesa una imagen de entrada mediante el modelo MoGe para generar una nube de puntos 3D, un mapa de profundidad, los intrínsecos de la cámara, una máscara y las normales de superficie.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `moge_model` | El modelo MoGe que se usará para la inferencia. | MOGE_MODEL | Sí | N/A |
| `image` | La imagen de entrada para la estimación de profundidad y geometría. Solo se utilizan los canales RGB; cualquier canal alfa se ignora. | IMAGE | Sí | N/A |
| `resolution_level` | Controla la resolución de procesamiento. 0 es el más rápido, 9 proporciona el mayor detalle. (por defecto: 9) | INT | Sí | 0 a 9 |
| `fov_x_degrees` | (Avanzado) Campo de visión horizontal de la cámara de origen en grados. Establece la distancia focal utilizada para desproyectar el mapa de profundidad a 3D. Establézcalo en 0.0 para recuperar automáticamente el campo de visión a partir de los puntos predichos. (por defecto: 0.0) | FLOAT | Sí | 0.0 a 170.0 |
| `batch_size` | Número de imágenes procesadas por llamada de inferencia. Reduzca este valor si se queda sin memoria al procesar videos largos o conjuntos de imágenes grandes. (por defecto: 4) | INT | Sí | 1 a 64 |
| `force_projection` | (Avanzado) Fuerza la proyección de los puntos predichos. (por defecto: True) | BOOLEAN | Sí | True/False |
| `apply_mask` | (Avanzado) Cuando está habilitado, establece los píxeles enmascarados (cielo o no válidos) a infinito en las salidas de puntos y profundidad. Esto ayuda a las herramientas de mallado a ignorar estas áreas. Desactívelo para mantener la geometría cruda predicha en todas partes; la máscara se devuelve por separado. (por defecto: True) | BOOLEAN | Sí | True/False |

Nota: La entrada `image` puede contener múltiples imágenes. El nodo las procesa en grupos de `batch_size` y combina los resultados en una única salida.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `moge_geometry` | Un diccionario que contiene la geometría estimada. Siempre incluye la `image` de entrada (solo canales RGB) y puede contener `points` (nube de puntos 3D), `depth` (mapa de profundidad), `intrinsics` (matriz de intrínsecos de la cámara), `mask` (máscara que identifica píxeles válidos) y `normal` (normales de superficie). | MOGE_GEOMETRY |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeInference/es.md)

---
**Source fingerprint (SHA-256):** `59f6b8b1ab65147a47f5dc7ebee7b965a5ab37c6a0843a2c80d50c767ad98db4`
