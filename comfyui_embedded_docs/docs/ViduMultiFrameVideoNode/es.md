# Generación de video multifotograma Vidu

Este nodo genera un video creando transiciones entre múltiples fotogramas clave. Comienza desde una imagen inicial y anima a través de una secuencia de imágenes finales e indicaciones definidas por el usuario, produciendo un único archivo de video como salida.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `modelo` | El modelo Vidu que se usará para la generación de video. | COMBO | Sí | "viduq2-pro"<br>"viduq2-turbo" |
| `imagen_inicial` | La imagen del fotograma inicial. La relación de aspecto debe estar entre 1:4 y 4:1. | IMAGE | Sí | Relación de aspecto 1:4 a 4:1 |
| `semilla` | Un valor de semilla para la generación de números aleatorios que garantice resultados reproducibles (predeterminado: 1). | INT | Sí | 0 a 2147483647 |
| `resolución` | La resolución del video de salida. | COMBO | Sí | "720p"<br>"1080p" |
| `fotogramas` | Número de transiciones de fotogramas clave (2-9). Al seleccionar un valor, se muestran dinámicamente las entradas necesarias para cada fotograma. | DYNAMIC_COMBO | Sí | "2"<br>"3"<br>"4"<br>"5"<br>"6"<br>"7"<br>"8"<br>"9" |

### Entradas de fotogramas (compartidas por todas las opciones de número de fotogramas)

Cuando `frames` se establece en un número, las siguientes tres entradas se muestran para cada fotograma `i` desde 1 hasta ese número. Por ejemplo, elegir "3" agrega `prompt1` / `end_image1` / `duration1`, `prompt2` / `end_image2` / `duration2`, y `prompt3` / `end_image3` / `duration3`.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `prompt{i}` | Indicación de texto para la transición del fotograma {i}. Campo de texto multilínea. Máximo 2000 caracteres. | STRING | Sí | Hasta 2000 caracteres |
| `end_image{i}` | Imagen del fotograma final para el segmento {i}. La relación de aspecto debe estar entre 1:4 y 4:1. | IMAGE | Sí | Relación de aspecto 1:4 a 4:1 |
| `duration{i}` | Duración del segmento {i} en segundos (predeterminado: 4). | INT | Sí | 2 a 7 |

**Notas:**

- Todas las entradas son obligatorias. `seed` tiene un valor predeterminado, pero sigue siendo una entrada obligatoria.
- `start_image` y cada `end_image{i}` deben tener una relación de aspecto entre 1:4 y 4:1.
- Cada `prompt{i}` tiene una longitud máxima de 2000 caracteres.
- Cada `duration{i}` debe estar entre 2 y 7 segundos.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `output` | El archivo de video generado que contiene todas las transiciones animadas. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduMultiFrameVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `ad877532ba27444938b7b2e4634ac7f8a47db0f7fb53967d874ad38b44336dcf`
