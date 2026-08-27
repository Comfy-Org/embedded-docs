# Ideogram P-Image

Ideogram & Pruna P-Image genera imágenes a partir de una indicación de texto utilizando el rápido modelo de texto a imagen de Ideogram, conocido por su gran manejo de tipografía y fotorrealismo. También admite descripciones JSON estructuradas de Ideogram 4.0 para un control exacto sobre cadenas de texto, colores y diseño. El nodo devuelve la(s) imagen(es) generada(s) junto con la indicación final a partir de la cual se generó realmente la imagen.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `prompt` | Indicación de texto. También acepta una descripción JSON estructurada de Ideogram 4.0 (colores exactos como hexadecimales #RRGGBB, cadenas de texto exactas, diseño de cuadro delimitador) — establezca prompt_upsampling en OFF para usarla tal cual. No debe estar vacía. (predeterminado: "") | STRING | Sí | Cualquier texto no vacío |
| `quality` | Nivel de velocidad/precio/calidad. MEDIUM es el valor predeterminado para uso cotidiano; HIGH para indicaciones complejas, detalles finos y texto difícil; VERY_LOW/LOW para borradores a gran escala. El texto difícil se renderiza mal por debajo de MEDIUM. (predeterminado: "MEDIUM") | COMBO | Sí | "VERY_LOW"<br>"LOW"<br>"MEDIUM"<br>"HIGH" |
| `resolution` | Clase de tamaño de salida (los píxeles exactos siguen la relación de aspecto; p. ej., 16:9 da 1280x720 en 1K y 2560x1440 en 2K). Prefiera HIGH + 2K para una tipografía nítida. (predeterminado: "1K") | COMBO | Sí | "1K"<br>"2K" |
| `aspect_ratio` | La relación de aspecto para la generación de imágenes. (predeterminado: "1:1") | COMBO | Sí | "1:3"<br>"3:1"<br>"1:2"<br>"2:1"<br>"9:16"<br>"16:9"<br>"10:16"<br>"16:10"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"4:5"<br>"5:4"<br>"1:1" |
| `prompt_upsampling` | Expande las indicaciones cortas a una descripción estructurada detallada antes de la generación (la indicación reescrita se devuelve como final_prompt). Establezca OFF cuando proporcione su propia descripción JSON o redacción exacta. (predeterminado: "AUTO") | COMBO | Sí | "AUTO"<br>"ON"<br>"OFF" |
| `seed` | Semilla para una generación reproducible. Con prompt_upsampling OFF, la misma semilla y configuración devuelven la misma imagen; con ON/AUTO la reescritura de la indicación varía en cada ejecución; reproduzca un resultado reutilizando su salida final_prompt con prompt_upsampling OFF y la misma semilla. (predeterminado: 42) | INT | No | 0 a 2147483647 |

**Nota sobre restricciones:** La indicación debe contener al menos un carácter que no sea un espacio en blanco; de lo contrario, el nodo falla. Establezca `prompt_upsampling` en OFF cuando proporcione su propia descripción JSON estructurada o redacción exacta. Cuando `prompt_upsampling` esté en ON o AUTO, la indicación se reescribe antes de la generación, por lo que la misma semilla puede no reproducir la misma imagen; para reproducir una imagen, reutilice su salida `final_prompt` con `prompt_upsampling` OFF y la misma semilla.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `image` | La(s) imagen(es) generada(s) se devuelve(n) como un lote de imágenes. Si el filtro de seguridad de contenido de Ideogram bloquea la generación, se lanza un error en su lugar. | IMAGE |
| `final_prompt` | La indicación a partir de la cual se generó realmente la imagen (la descripción estructurada reescrita cuando prompt_upsampling se ejecutó; de lo contrario, su indicación original). Vuelva a introducirla con prompt_upsampling OFF y la misma semilla para reproducir esta imagen. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPImage/es.md)

---
**Source fingerprint (SHA-256):** `6b014c2f097c49b5930f38869a4e2da0ebb19863763ae5817d6e566a36d2b8e8`
