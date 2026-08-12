# TopazImageEnhanceV2

Topaz Image Enhance aplica el escalado y la mejora de imagen estándar de la industria a una única imagen de entrada utilizando los modelos de Topaz. Envía la imagen a la API de Topaz, la procesa con el modelo seleccionado y devuelve el resultado mejorado. Se puede elegir entre tres modelos: Reimagine, Bloom 2 y Wonder 3.5.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `image` | La imagen de entrada a mejorar. Solo se admite una imagen de entrada. | IMAGE | Sí | Imagen única |
| `model` | El modelo de mejora de Topaz a utilizar. El modelo seleccionado determina qué ajustes específicos del modelo aparecen. | STRING | Sí | `"Reimagine"`<br>`"Bloom 2"`<br>`"Wonder 3.5"` |
| `output_width` | Un valor de cero indica que se calcula automáticamente (normalmente será el tamaño original o se escalará proporcionalmente a `output_height` si se especifica). Wonder 3.5 solo admite factores de ampliación de 1x a 6x. Bloom 2 y Wonder 3.5 conservan la relación de aspecto de entrada y tratan el tamaño solicitado como un objetivo. (por defecto: 0) | INT | No | 0 a 32000 |
| `output_height` | Un valor de cero indica que se generará con la misma altura que la original o se escalará proporcionalmente a `output_width` si se especifica. Wonder 3.5 solo admite factores de ampliación de 1x a 6x. Bloom 2 y Wonder 3.5 conservan la relación de aspecto de entrada y tratan el tamaño solicitado como un objetivo. (por defecto: 0) | INT | No | 0 a 32000 |

### Ajustes de Reimagine

Estos ajustes se aplican cuando `model` está establecido en `"Reimagine"`.

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `prompt` | Indicación de texto opcional para guiar la ampliación creativa. (por defecto: "") | STRING | Sí | Cualquier texto |
| `creativity` | Nivel de creatividad para la mejora. (por defecto: 3) | INT | Sí | 1 a 9 |
| `subject_detection` | Modo de detección de sujetos. | STRING | Sí | `"All"`<br>`"Foreground"`<br>`"Background"` |
| `face_enhancement` | Mejora los rostros (si los hay) durante el procesamiento. (por defecto: True) | BOOLEAN | Sí | true<br>false |
| `face_enhancement_creativity` | Define el nivel de creatividad para la mejora de rostros. (por defecto: 0.0) | FLOAT | Sí | 0.0 a 1.0 |
| `face_enhancement_strength` | Controla la nitidez de los rostros mejorados en relación con el fondo. (por defecto: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `face_preservation` | Preserva la identidad facial de los sujetos. (por defecto: True) | BOOLEAN | Sí | true<br>false |
| `color_preservation` | Preserva los colores originales. (por defecto: True) | BOOLEAN | Sí | true<br>false |
| `crop_to_fill` | De forma predeterminada, la imagen se muestra con barras (letterbox) cuando la relación de aspecto de salida difiere. Activa esta opción para recortar la imagen y llenar las dimensiones de salida. (por defecto: False) | BOOLEAN | Sí | true<br>false |

### Ajustes de Bloom 2

Estos ajustes se aplican cuando `model` está establecido en `"Bloom 2"`.

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `prompt` | Indicación de texto opcional para la generación. Si se deja vacío, se genera automáticamente una indicación a partir de la imagen de entrada. (por defecto: "") | STRING | Sí | Cualquier texto |
| `creativity` | 1 es una mejora moderada, 9 es una reinterpretación marcada con detalles recién generados. (por defecto: 3) | INT | Sí | 1 a 9 |
| `seed` | Semilla para una generación reproducible. (por defecto: 2) | INT | Sí | 1 a 2000 |
| `color_preservation` | Preserva los colores originales. (por defecto: True) | BOOLEAN | Sí | true<br>false |
| `grain` | Añade grano a la imagen de salida. (por defecto: False) | BOOLEAN | Sí | true<br>false |
| `grain_model` | Modelo de grano a utilizar. Se ignora si el grano está desactivado. | STRING | Sí | `"silver"`<br>`"gaussian"`<br>`"grey"` |
| `grain_strength` | Fuerza del efecto de grano. Se ignora si el grano está desactivado. (por defecto: 0.5) | FLOAT | Sí | 0.0 a 1.0 |
| `grain_size` | Tamaño de las partículas de grano. Se ignora si el grano está desactivado. (por defecto: 1.0) | FLOAT | Sí | 1.0 a 5.0 |
| `grain_density` | Densidad del efecto de grano. Se ignora si el grano está desactivado. (por defecto: 0.5) | FLOAT | Sí | 0.0 a 1.0 |

### Ajustes de Wonder 3.5

Estos ajustes se aplican cuando `model` está establecido en `"Wonder 3.5"`.

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `enhancement_strength` | Nivel de mejora para distintas condiciones de entrada. (por defecto: "high") | STRING | Sí | `"low"`<br>`"medium"`<br>`"high"` |
| `grain` | Añade grano a la imagen de salida. (por defecto: False) | BOOLEAN | Sí | true<br>false |
| `grain_model` | Modelo de grano a utilizar. Se ignora si el grano está desactivado. | STRING | Sí | `"silver"`<br>`"gaussian"`<br>`"grey"` |
| `grain_strength` | Fuerza del efecto de grano. Se ignora si el grano está desactivado. (por defecto: 0.5) | FLOAT | Sí | 0.0 a 1.0 |
| `grain_size` | Tamaño de las partículas de grano. Se ignora si el grano está desactivado. (por defecto: 1.0) | FLOAT | Sí | 1.0 a 5.0 |
| `grain_density` | Densidad del efecto de grano. Se ignora si el grano está desactivado. (por defecto: 0.5) | FLOAT | Sí | 0.0 a 1.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `IMAGE` | La imagen mejorada y ampliada devuelta por la API de Topaz. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhanceV2/es.md)

---
**Source fingerprint (SHA-256):** `4301abb7cbab5122490b2ed3b328b199a29409da0dcc5ea5201570c2acbc2a58`
