# Construir prompt JSON (Ideogram)

Este nodo construye un prompt JSON estructurado, formateado específicamente para el modelo de generación de imágenes Ideogram 4. Organiza tus instrucciones de texto, preferencias de estilo y paleta de colores en la estructura JSON requerida que el modelo espera.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `elemento` | Elementos del prompt provenientes del nodo Crear Cajas Delimitadoras. | ARRAY | Sí | - |
| `descripción_general` | Descripción opcional de la imagen en una o dos oraciones. Altamente recomendada. (predeterminado: vacío) | STRING | No | - |
| `fondo` | Descripción obligatoria del fondo o entorno de la imagen. (predeterminado: vacío) | STRING | Sí | - |
| `estilo` | La categoría de estilo visual para la imagen generada. (predeterminado: "none") | COMBO | Sí | `"none"`<br>`"photo"`<br>`"art_style"` |
| `photo` | Detalles de cámara o lente para salidas fotográficas (ej. 35mm, f/1.4, bokeh). Solo disponible cuando el estilo está configurado como "photo". (predeterminado: vacío) | STRING | No | - |
| `art_style` | Descripción del estilo artístico (ej. ilustración vectorial plana, contornos gruesos). Solo disponible cuando el estilo está configurado como "art_style". (predeterminado: vacío) | STRING | No | - |
| `estética` | Palabras clave estéticas obligatorias (ej. melancólico, cinematográfico, desaturado). (predeterminado: vacío) | STRING | Sí | - |
| `iluminación` | Descripción obligatoria de la iluminación (ej. hora dorada, luz de borde, sombras dramáticas). (predeterminado: vacío) | STRING | Sí | - |
| `medio` | Tipo de medio obligatorio (ej. fotografía, ilustración, render_3d, pintura, diseño_gráfico). Cuando el estilo es photo, configurar como photograph. (predeterminado: vacío) | STRING | Sí | - |
| `paleta_de_colores` | Códigos de color hexadecimales que guían los colores dominantes de la imagen. Hasta 16 entradas. | COLORS | No | - |

**Nota:** Cuando el parámetro `style` está configurado como "photo", la entrada `photo` estará disponible y debes configurar el parámetro `medium` como "photograph". Cuando `style` está configurado como "art_style", la entrada `art_style` estará disponible.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `prompt` | Un diccionario JSON estructurado que contiene la descripción de alto nivel, la descripción del estilo (si aplica) y la descomposición compositiva con fondo y elementos. | DICT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BuildJsonPromptIdeogram/es.md)

---
**Source fingerprint (SHA-256):** `56a045e0c7c19531e6443696c0bdf3946df066d03eea7d2d217b7d92f052592f`
