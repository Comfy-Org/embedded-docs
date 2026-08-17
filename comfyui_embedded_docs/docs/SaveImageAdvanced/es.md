# Guardar imagen (avanzado)

El nodo **SaveImageAdvanced** guarda imágenes en el directorio de salida de ComfyUI con control avanzado sobre el formato de archivo, la profundidad de bits y el espacio de color. Admite guardar archivos PNG o EXR y puede incrustar metadatos del flujo de trabajo en los archivos guardados.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `images` | Las imágenes a guardar. | IMAGE | Sí | - |
| `filename_prefix` | El prefijo para el archivo a guardar. Puede incluir tokens de formato como `%date:yyyy-MM-dd%` o `%Empty Latent Image.width%`. (por defecto: "ComfyUI") | STRING | Sí | - |
| `format` | El formato de archivo en el que se guardará la imagen. Seleccionar un formato muestra opciones adicionales para ese formato. | DYNAMIC_COMBO | Sí | `"png"`<br>`"exr"` |

### Entradas de PNG

Estas entradas se muestran cuando `format` está establecido en `"png"`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `bit_depth` | La profundidad de bits utilizada al guardar la imagen. (por defecto: "8-bit") | COMBO | Sí (condicional) | `"8-bit"`<br>`"16-bit"` |
| `input_color_space` | El espacio de color del tensor de entrada. (por defecto: "sRGB") | COMBO | Sí (condicional) | `"sRGB"` |

### Entradas de EXR

Estas entradas se muestran cuando `format` está establecido en `"exr"`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `bit_depth` | La profundidad de bits utilizada al guardar la imagen. (por defecto: "32-bit float") | COMBO | Sí (condicional) | `"32-bit float"` |
| `input_color_space` | Espacio de color del tensor de entrada. El EXR siempre se escribe como lineal de escena en la gama correspondiente. (por defecto: "sRGB") | COMBO | Sí (condicional) | `"sRGB"`<br>`"HDR"`<br>`"linear"` |

**Notas sobre las dependencias de parámetros y el comportamiento de los archivos:**

- `bit_depth` e `input_color_space` solo aparecen cuando su `format` principal está seleccionado.
- Para el formato PNG, solo están disponibles las profundidades de bits `"8-bit"` y `"16-bit"`, y únicamente el espacio de color `"sRGB"`. La selección del espacio de color no modifica los píxeles PNG: los archivos PNG siempre se guardan como imágenes codificadas en sRGB.
- Para el formato EXR, solo está disponible la profundidad de bits `"32-bit float"`, con espacios de color `"sRGB"`, `"HDR"` o `"linear"`.
- El parámetro `input_color_space` para EXR determina cómo se interpreta el tensor de entrada antes de guardar:
  - `"sRGB"` — la entrada está codificada en sRGB Rec.709; se aplica la EOTF inversa de sRGB.
  - `"HDR"` — la entrada está codificada en HLG Rec.2020 (BT.2100); se aplica la OETF inversa de HLG para obtener luz lineal de escena.
  - `"linear"` — la entrada ya es lineal de escena (primarios Rec.709); se escribe sin cambios. Úselo para la salida de renderizador/compositor.
- Los metadatos del flujo de trabajo (el prompt e información PNG adicional) se incrustan en los archivos PNG y EXR guardados, a menos que la escritura de metadatos esté desactivada mediante el argumento de línea de comandos `--disable-metadata`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `images` | Las imágenes que se guardaron (las mismas imágenes pasadas a la entrada `images`). El resultado del nodo en la interfaz de usuario incluye una lista de los archivos guardados, cada uno con su nombre de archivo, subcarpeta y tipo ("output"). | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageAdvanced/es.md)

---
**Source fingerprint (SHA-256):** `b03a822a90cf50d30fbf4397ab280393951f08d2339dd48c0dbaf75d9c415bca`
