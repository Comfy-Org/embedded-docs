# SaveImageAdvanced

El nodo **SaveImageAdvanced** guarda imágenes en tu directorio de salida de ComfyUI con control avanzado sobre el formato de archivo, profundidad de bits y espacio de color. Admite guardar como archivos PNG o EXR y puede incrustar metadatos del flujo de trabajo en los archivos guardados.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `imágenes` | Las imágenes a guardar. | IMAGE | Sí | - |
| `prefijo_nombre_archivo` | El prefijo para el archivo a guardar. Puede incluir tokens de formato como `%date:yyyy-MM-dd%` o `%Empty Latent Image.width%`. (predeterminado: "ComfyUI") | STRING | Sí | - |
| `formato` | El formato de archivo en el que se guardará la imagen. Seleccionar un formato revela opciones adicionales para ese formato. | COMBO | Sí | `"png"`<br>`"exr"` |
| `bit_depth` | La profundidad de bits para el formato seleccionado. Este parámetro aparece cuando se elige un formato. (predeterminado: "8-bit" para PNG, "32-bit float" para EXR) | COMBO | Sí (condicional) | Para PNG: `"8-bit"`<br>`"16-bit"`<br>Para EXR: `"32-bit float"` |
| `input_color_space` | Espacio de color del tensor de entrada. Para PNG, solo está disponible sRGB. Para EXR, la imagen siempre se escribe como lineal de escena en la gama correspondiente. (predeterminado: "sRGB") | COMBO | Sí (condicional) | Para PNG: `"sRGB"`<br>Para EXR: `"sRGB"`<br>`"HDR"`<br>`"linear"` |

**Notas sobre dependencias de parámetros:**
- Los parámetros `bit_depth` e `input_color_space` solo están disponibles cuando se selecciona un `format` específico.
- Para el formato PNG, solo están disponibles las profundidades de bits "8-bit" y "16-bit", y únicamente el espacio de color "sRGB".
- Para el formato EXR, solo está disponible la profundidad de bits "32-bit float", con espacios de color "sRGB", "HDR" o "linear".
- El parámetro `input_color_space` para EXR determina cómo se interpreta el tensor de entrada:
  - `"sRGB"` — la entrada es Rec.709 codificada en sRGB; se aplica la EOTF inversa de sRGB.
  - `"HDR"` — la entrada es Rec.2020 (BT.2100) codificada en HLG; se aplica la OETF inversa de HLG para obtener luz lineal de escena.
  - `"linear"` — la entrada ya es lineal de escena (primarios Rec.709); se escribe sin cambios. Úsalo para salidas de renderizador/compositor.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `imágenes` | Una lista de resultados de imágenes guardadas, cada una contiene el nombre de archivo, subcarpeta y tipo ("output"). Esta salida se utiliza para fines de visualización en la interfaz de usuario. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageAdvanced/es.md)

---
**Source fingerprint (SHA-256):** `61e52bab8c28437cf648e4790823c15dbe0f758478635b0bd8b5cce785421fe5`
