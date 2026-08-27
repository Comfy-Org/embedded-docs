# Guardar imagen (avanzado)

El nodo **Save Image (Advanced)** guarda las imágenes de entrada en el directorio de salida de ComfyUI con control avanzado sobre el formato de archivo, la profundidad de bits y el espacio de color. Es compatible con el guardado como archivos PNG o EXR y puede incrustar metadatos del flujo de trabajo en los archivos guardados.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `imágenes` | Las imágenes a guardar. | IMAGE | Sí | - |
| `prefijo_nombre_archivo` | El prefijo para el archivo a guardar. Puede incluir tokens de formato como `%date:yyyy-MM-dd%` o `%Empty Latent Image.width%`. (predeterminado: "ComfyUI") | STRING | Sí | - |
| `formato` | El formato de archivo en el que se guardará la imagen. Al seleccionar un formato, se muestran opciones adicionales para ese formato. | DYNAMIC_COMBO | Sí | `"png"`<br>`"exr"` |

### Entradas de PNG

Estas opciones aparecen cuando `format` está establecido en `"png"`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `bit_depth` | La profundidad de bits para el archivo PNG guardado. (predeterminado: "8-bit") | COMBO | Sí (condicional) | `"8-bit"`<br>`"16-bit"` |
| `input_color_space` | Espacio de color del tensor de entrada. Solo sRGB está disponible para el formato PNG. (predeterminado: "sRGB") | COMBO | Sí (condicional) | `"sRGB"` |

### Entradas de EXR

Estas opciones aparecen cuando `format` está establecido en `"exr"`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `bit_depth` | La profundidad de bits para el archivo EXR guardado. (predeterminado: "32-bit float") | COMBO | Sí (condicional) | `"32-bit float"` |
| `input_color_space` | Espacio de color del tensor de entrada. El EXR siempre se escribe como lineal de escena en la gama correspondiente.<br>`"sRGB"` — la entrada está codificada en sRGB Rec.709; se aplica la EOTF sRGB inversa.<br>`"HDR"` — la entrada está codificada en HLG Rec.2020 (BT.2100); se aplica la OETF HLG inversa para obtener luz lineal de escena.<br>`"linear"` — la entrada ya es lineal de escena (primarios Rec.709); se escribe sin cambios. Utilícelo para salida de renderizador/compositor. (predeterminado: "sRGB") | COMBO | Sí (condicional) | `"sRGB"`<br>`"HDR"`<br>`"linear"` |

**Notas sobre dependencias de parámetros:**
- Los parámetros `bit_depth` e `input_color_space` solo están disponibles cuando se selecciona un `format` específico.
- Para el formato PNG, solo están disponibles las profundidades de bits "8-bit" y "16-bit", y solo el espacio de color "sRGB".
- Para el formato EXR, solo está disponible la profundidad de bits "32-bit float", con espacios de color "sRGB", "HDR" o "linear".
- Las imágenes deben tener 1 (escala de grises), 3 (RGB) o 4 (RGBA) canales; no se admiten otras cantidades de canales y generan un error.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `images` | Las imágenes de entrada, que se transmiten sin cambios. La salida de la interfaz de usuario del nodo proporciona una lista de resultados de imágenes guardadas, cada uno con el nombre de archivo, la subcarpeta y el tipo ("output"). | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageAdvanced/es.md)

---
**Source fingerprint (SHA-256):** `b03a822a90cf50d30fbf4397ab280393951f08d2339dd48c0dbaf75d9c415bca`
