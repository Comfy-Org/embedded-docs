> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaImageEditNode/es.md)

El nodo **Bria FIBO Image Edit** permite modificar una imagen existente mediante una instrucción de texto. Envía la imagen y tu indicación a la API de Bria, que utiliza el modelo FIBO para generar una nueva versión editada de la imagen según tu solicitud. También puedes proporcionar una máscara para limitar las ediciones a un área específica.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `model` | COMBO | Sí | `"FIBO"` | La versión del modelo a utilizar para la edición de imágenes. |
| `image` | IMAGE | Sí | - | La imagen de entrada que deseas editar. |
| `prompt` | STRING | No | - | La instrucción de texto que describe cómo editar la imagen (predeterminado: vacío). |
| `negative_prompt` | STRING | No | - | Texto que describe lo que no deseas que aparezca en la imagen editada (predeterminado: vacío). |
| `structured_prompt` | STRING | No | - | Una cadena que contiene la indicación de edición estructurada en formato JSON. Úsalo en lugar de la indicación habitual para un control preciso y programático (predeterminado: vacío). |
| `seed` | INT | Sí | 1 a 2147483647 | Número utilizado para inicializar la generación aleatoria, garantizando resultados reproducibles (predeterminado: 1). |
| `guidance_scale` | FLOAT | Sí | 3.0 a 5.0 | Controla qué tan fielmente la imagen generada sigue la indicación. Un valor más alto resulta en una adherencia más fuerte (predeterminado: 3.0). |
| `steps` | INT | Sí | 20 a 50 | El número de pasos de eliminación de ruido que realizará el modelo (predeterminado: 50). |
| `moderation` | DYNAMICCOMBO | Sí | `"false"`<br>`"true"` | Habilita o deshabilita la moderación de contenido. Seleccionar `"true"` revela opciones adicionales de moderación para el contenido de la indicación, la entrada visual y la salida visual. |
| `mask` | MASK | No | - | Una imagen de máscara opcional. Si se proporciona, las ediciones solo se aplicarán a las áreas enmascaradas de la imagen. |

**Restricciones importantes:**

* Debes proporcionar al menos una de las entradas `prompt` o `structured_prompt`. No pueden estar ambas vacías.
* Se requiere exactamente una entrada `image`.
* Cuando el parámetro `moderation` está configurado como `"true"`, tres entradas booleanas adicionales están disponibles: `prompt_content_moderation` (predeterminado: false), `visual_input_moderation` (predeterminado: false) y `visual_output_moderation` (predeterminado: true).

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `IMAGE` | IMAGE | La imagen editada devuelta por la API de Bria. |
| `structured_prompt` | STRING | La indicación estructurada que se utilizó o generó durante el proceso de edición. |

---
**Source fingerprint (SHA-256):** `30148261f43f5bfd14339f5ff1ec250381a615cc05c67eee21b0a2423ebe349d`
