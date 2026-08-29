# Guardar imagen (avanzado)

El nodo **Save Image (Advanced)** guarda las imágenes de entrada en el directorio de salida de ComfyUI con control avanzado sobre el formato de archivo, la profundidad de bits y el espacio de color. Permite guardar archivos PNG, EXR o AVIF (incluido AVIF animado) y puede incrustar metadatos del flujo de trabajo en los archivos guardados.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `imágenes` | Las imágenes que se van a guardar. | IMAGE | Sí | - |
| `prefijo_nombre_archivo` | El prefijo del archivo que se va a guardar. Puede incluir tokens de formato como `%date:yyyy-MM-dd%` o `%Empty Latent Image.width%`. (por defecto: "ComfyUI") | STRING | Sí | - |
| `formato` | El formato de archivo en el que se guardará la imagen. Al seleccionar un formato se muestran opciones adicionales para ese formato. | DYNAMIC_COMBO | Sí | `"png"`<br>`"exr"`<br>`"avif"` |

### Entradas de PNG

Estas opciones aparecen cuando `format` se establece en `"png"`.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `bit_depth` | La profundidad de bits del archivo PNG guardado. (por defecto: "8-bit") | COMBO | Sí (condicional) | `"8-bit"`<br>`"16-bit"` |
| `input_color_space` | Espacio de color del tensor de entrada. Solo sRGB está disponible para el formato PNG. (por defecto: "sRGB") | COMBO | Sí (condicional) | `"sRGB"` |

### Entradas de EXR

Estas opciones aparecen cuando `format` se establece en `"exr"`.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `bit_depth` | La profundidad de bits del archivo EXR guardado. (por defecto: "32-bit float") | COMBO | Sí (condicional) | `"32-bit float"` |
| `input_color_space` | Espacio de color del tensor de entrada. El archivo EXR siempre se escribe como lineal de escena en la gama correspondiente.<br>`"sRGB"` — la entrada está codificada en sRGB (Rec.709); se aplica la EOTF inversa de sRGB.<br>`"HDR"` — la entrada está codificada en HLG (Rec.2020, BT.2100); se aplica la OETF inversa de HLG para obtener luz lineal de escena.<br>`"linear"` — la entrada ya es lineal de escena (primarios Rec.709); se escribe tal cual. Use esto para la salida de renderizadores/compositores. (por defecto: "sRGB") | COMBO | Sí (condicional) | `"sRGB"`<br>`"HDR"`<br>`"linear"` |

### Entradas de AVIF

Estas opciones aparecen cuando `format` se establece en `"avif"`.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `bit_depth` | La profundidad de bits del archivo AVIF guardado. Auto usa YUV420 de 8 bits para sRGB y YUV420 de 10 bits para HDR. (por defecto: "auto") | COMBO | Sí (condicional) | `"auto"`<br>`"8-bit YUV420"`<br>`"10-bit YUV420"` |
| `input_color_space` | Espacio de color de las imágenes de entrada. HDR selecciona BT.2020/HLG y HDR PQ selecciona BT.2020/PQ. (por defecto: "sRGB") | COMBO | Sí (condicional) | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |
| `crf` | Los valores más bajos producen mayor calidad y archivos más grandes. (por defecto: 18) | INT | Sí (condicional) | 1 a 63 |
| `save_mode` | El modo de guardado del archivo AVIF. `"still images"` guarda cada imagen del lote como un archivo de imagen fija separado; `"animated"` guarda el lote completo como un único archivo AVIF animado y muestra `fps` y `loop_count`. (por defecto: "still images") | DYNAMIC_COMBO | Sí (condicional) | `"still images"`<br>`"animated"` |

### Opciones de AVIF animado

Estas opciones aparecen cuando `save_mode` se establece en `"animated"`.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `fps` | La velocidad de fotogramas de la animación. (por defecto: 6.0) | FLOAT | Sí (condicional) | 0.01 a 1000.0 |
| `loop_count` | Número de veces que se repite la animación. 0 la repite indefinidamente. (por defecto: 0) | INT | Sí (condicional) | 0 a 1000 |

**Notas sobre las dependencias de los parámetros:**
- Los parámetros específicos del formato (`bit_depth`, `input_color_space`, y para AVIF también `crf` y `save_mode`) solo están disponibles cuando se selecciona un `format` específico.
- Para el formato PNG, solo están disponibles las profundidades de bits "8-bit" y "16-bit", y únicamente el espacio de color "sRGB".
- Para el formato EXR, solo está disponible la profundidad de bits "32-bit float", con espacios de color "sRGB", "HDR" o "linear".
- Para el formato AVIF, `fps` y `loop_count` solo están disponibles cuando `save_mode` se establece en `"animated"`.
- Las imágenes PNG y EXR deben tener 1 (escala de grises), 3 (RGB) o 4 (RGBA) canales; otros números de canales no son compatibles y generan un error.
- AVIF solo admite imágenes en escala de grises de 1 canal e imágenes RGB de 3 canales; las imágenes RGBA (con canal alfa) no son compatibles y generan un error.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `images` | Las imágenes de entrada se pasan sin cambios. La salida de la interfaz de usuario del nodo proporciona una lista de los resultados de imágenes guardadas, cada uno con el nombre de archivo, la subcarpeta y el tipo ("output"). | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageAdvanced/es.md)

---
**Source fingerprint (SHA-256):** `d3df3caca99d58d973d0bc2ff7c22c4626185d390ec2acf870d4014331c4c335`
