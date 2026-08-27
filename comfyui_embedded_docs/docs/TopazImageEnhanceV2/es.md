# Mejora de Imagen Topaz

Topaz Image Enhance aplica ampliación de escala y mejora de imagen de nivel profesional a una sola imagen de entrada mediante los modelos de Topaz. Envía la imagen a la API de Topaz, la procesa con el modelo seleccionado y devuelve el resultado mejorado. Puede elegir entre tres modelos: Reimagine, Bloom 2 y Wonder 3.5.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `image` | La imagen de entrada a mejorar. Solo se admite una imagen de entrada. | IMAGE | Sí | Imagen única |
| `model` | El modelo de mejora de Topaz a utilizar. El modelo seleccionado determina qué ajustes específicos del modelo aparecen. | DYNAMIC_COMBO | Sí | `"Reimagine"`<br>`"Bloom 2"`<br>`"Wonder 3.5"` |
| `output_width` | Un valor de cero significa calcular automáticamente (normalmente será el tamaño original o escalado proporcionalmente a `output_height` si se especifica). Wonder 3.5 solo admite factores de ampliación de 1x a 6x. Bloom 2 y Wonder 3.5 conservan la relación de aspecto de la entrada y tratan el tamaño solicitado como un objetivo. (por defecto: 0) | INT | No | 0 a 32000 |
| `output_height` | Un valor de cero significa usar la misma altura que la original o escalada proporcionalmente a `output_width` si se especifica. Wonder 3.5 solo admite factores de ampliación de 1x a 6x. Bloom 2 y Wonder 3.5 conservan la relación de aspecto de la entrada y tratan el tamaño solicitado como un objetivo. (por defecto: 0) | INT | No | 0 a 32000 |

### Entradas de Reimagine

Estos ajustes se aplican cuando `model` está establecido en `"Reimagine"`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `prompt` | Indicación de texto opcional para guiar la ampliación creativa. (por defecto: "") | STRING | Sí | Cualquier texto |
| `creativity` | Nivel de creatividad para la mejora. (por defecto: 3) | INT | Sí | 1 a 9 |
| `subject_detection` | Modo de detección de sujeto. | COMBO | Sí | `"All"`<br>`"Foreground"`<br>`"Background"` |
| `face_enhancement` | Mejora los rostros (si están presentes) durante el procesamiento. (por defecto: True) | BOOLEAN | Sí | true<br>false |
| `face_enhancement_creativity` | Establece el nivel de creatividad para la mejora de rostros. (por defecto: 0.0) | FLOAT | Sí | 0.0 a 1.0 |
| `face_enhancement_strength` | Controla la nitidez de los rostros mejorados en relación con el fondo. (por defecto: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `face_preservation` | Conserva la identidad facial de los sujetos. (por defecto: True) | BOOLEAN | Sí | true<br>false |
| `color_preservation` | Conserva los colores originales. (por defecto: True) | BOOLEAN | Sí | true<br>false |
| `crop_to_fill` | De forma predeterminada, la imagen se muestra con barras negras (letterbox) cuando la relación de aspecto de salida difiere. Actívalo para recortar la imagen y rellenar las dimensiones de salida. (por defecto: False) | BOOLEAN | Sí | true<br>false |

### Entradas de Bloom 2

Estos ajustes se aplican cuando `model` está establecido en `"Bloom 2"`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `prompt` | Indicación de texto opcional para la generación. Déjalo vacío para generar automáticamente una indicación a partir de la imagen de entrada. (por defecto: "") | STRING | Sí | Cualquier texto |
| `creativity` | 1 es una mejora moderada, 9 es una reinterpretación marcada con nuevos detalles generados. (por defecto: 3) | INT | Sí | 1 a 9 |
| `seed` | Semilla para una generación reproducible. (por defecto: 2) | INT | Sí | 1 a 2000 |
| `color_preservation` | Conserva los colores originales. (por defecto: True) | BOOLEAN | Sí | true<br>false |
| `grain` | Añade grano a la imagen de salida. (por defecto: False) | BOOLEAN | Sí | true<br>false |
| `grain_model` | Modelo de grano a utilizar. Se ignora si el grano está desactivado. | COMBO | Sí | `"silver"`<br>`"gaussian"`<br>`"grey"` |
| `grain_strength` | Fuerza del efecto de grano. Se ignora si el grano está desactivado. (por defecto: 0.5) | FLOAT | Sí | 0.0 a 1.0 |
| `grain_size` | Tamaño de las partículas de grano. Se ignora si el grano está desactivado. (por defecto: 1.0) | FLOAT | Sí | 1.0 a 5.0 |
| `grain_density` | Intensidad del efecto de grano. Se ignora si el grano está desactivado. (por defecto: 0.5) | FLOAT | Sí | 0.0 a 1.0 |

### Entradas de Wonder 3.5

Estos ajustes se aplican cuando `model` está establecido en `"Wonder 3.5"`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `enhancement_strength` | Nivel de mejora para condiciones de entrada variables. (por defecto: "high") | COMBO | Sí | `"low"`<br>`"medium"`<br>`"high"` |
| `grain` | Añade grano a la imagen de salida. (por defecto: False) | BOOLEAN | Sí | true<br>false |
| `grain_model` | Modelo de grano a utilizar. Se ignora si el grano está desactivado. | COMBO | Sí | `"silver"`<br>`"gaussian"`<br>`"grey"` |
| `grain_strength` | Fuerza del efecto de grano. Se ignora si el grano está desactivado. (por defecto: 0.5) | FLOAT | Sí | 0.0 a 1.0 |
| `grain_size` | Tamaño de las partículas de grano. Se ignora si el grano está desactivado. (por defecto: 1.0) | FLOAT | Sí | 1.0 a 5.0 |
| `grain_density` | Intensidad del efecto de grano. Se ignora si el grano está desactivado. (por defecto: 0.5) | FLOAT | Sí | 0.0 a 1.0 |

**Nota:** Solo se admite una imagen de entrada. Los ajustes de grano (`grain_model`, `grain_strength`, `grain_size`, `grain_density`) se ignoran a menos que `grain` esté habilitado. Para Bloom 2, dejar `prompt` vacío genera automáticamente una indicación a partir de la imagen de entrada. Wonder 3.5 solo admite factores de ampliación de 1x a 6x; Bloom 2 y Wonder 3.5 conservan la relación de aspecto de la entrada y tratan el tamaño solicitado como un objetivo.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `IMAGE` | La imagen mejorada y ampliada devuelta por la API de Topaz. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhanceV2/es.md)

---
**Source fingerprint (SHA-256):** `19bb03ca7354f1b0d1e559b742b83939678fce6d5f490b1030717b846043e0e6`
