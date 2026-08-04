# IdeogramPImage

Ideogram P-Image genera imágenes a partir de un prompt de texto utilizando el modelo rápido de texto a imagen de Ideogram, conocido por su sólida tipografía y fotorrealismo. También admite subtítulos JSON estructurados de Ideogram 4.0 para un control exacto sobre cadenas de texto, colores y diseño. El nodo devuelve la(s) imagen(es) generada(s) junto con el prompt final del que realmente se generó la imagen.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `prompt` | Prompt de texto. También acepta un subtítulo JSON estructurado de Ideogram 4.0 (colores exactos como hexadecimanes #RRGGBB, cadenas de texto exactas, disposición mediante cuadros delimitadores) — configura prompt_upsampling en OFF para usarlo tal cual. No debe estar vacío. (por defecto: "") | STRING | Sí | Cualquier texto |
| `quality` | Nivel de velocidad/precio/calidad. MEDIUM es el predeterminado para uso diario; HIGH para prompts complejos, detalles finos y texto difícil; VERY_LOW/LOW para borradores a gran escala. El texto difícil se renderiza mal por debajo de MEDIUM. (por defecto: "MEDIUM") | STRING | Sí | "VERY_LOW"<br>"LOW"<br>"MEDIUM"<br>"HIGH" |
| `resolution` | Clase de tamaño de salida (los píxeles exactos siguen la relación de aspecto, p. ej., 16:9 da 1280x720 a 1K y 2560x1440 a 2K). Prefiere HIGH + 2K para tipografía nítida. (por defecto: "1K") | STRING | Sí | "1K"<br>"2K" |
| `aspect_ratio` | La relación de aspecto para la generación de imágenes. (por defecto: "1:1") | STRING | Sí | "1:3"<br>"3:1"<br>"1:2"<br>"2:1"<br>"9:16"<br>"16:9"<br>"10:16"<br>"16:10"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"4:5"<br>"5:4"<br>"1:1" |
| `prompt_upsampling` | Expande los prompts cortos en un subtítulo estructurado detallado antes de la generación (el prompt reescrito se devuelve como final_prompt). Configúralo en OFF cuando proporciones tu propio subtítulo JSON o redacción exacta. (por defecto: "AUTO") | STRING | Sí | "AUTO"<br>"ON"<br>"OFF" |
| `seed` | Semilla para generación reproducible. Con prompt_upsampling OFF, la misma semilla y configuración devuelven la misma imagen; con ON/AUTO la reescritura del prompt varía en cada ejecución — reproduce un resultado reutilizando su salida final_prompt con prompt_upsampling OFF y la misma semilla. (por defecto: 42) | INT | No | 0 a 2147483647 |

**Nota sobre limitaciones:** El prompt debe contener al menos un carácter que no sea un espacio en blanco; de lo contrario, el nodo falla. Configura `prompt_upsampling` en OFF cuando proporciones tu propio subtítulo JSON estructurado o redacción exacta. Cuando `prompt_upsampling` está en ON o AUTO, el prompt se reescribe antes de la generación, por lo que la misma semilla puede no reproducir la misma imagen; para reproducir una imagen, reutiliza su salida `final_prompt` con `prompt_upsampling` OFF y la misma semilla.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `image` | La(s) imagen(es) generada(s) devueltas como un lote de imágenes. Si el filtro de seguridad de contenido de Ideogram bloquea la generación, se genera un error en su lugar. | IMAGE |
| `final_prompt` | El prompt del cual se generó realmente la imagen (el subtítulo estructurado reescrito cuando prompt_upsampling se ejecutó, o tu prompt en caso contrario). Vuelve a introducirlo con prompt_upsampling OFF y la misma semilla para reproducir esta imagen. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPImage/es.md)

---
**Source fingerprint (SHA-256):** `7bd20aae508fee111ded32e87119ed6fc01c5ad5ba7d595e24391830a0f20bb7`
