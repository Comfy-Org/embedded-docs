# Edición de Imagen Bria

El nodo Bria FIBO Image Edit te permite modificar una imagen existente mediante una instrucción de texto. Envía la imagen y tu prompt a la API de Bria, que utiliza el modelo FIBO para generar una nueva versión editada de la imagen según tu solicitud. También puedes proporcionar una máscara para limitar las ediciones a un área específica.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `model` | La versión del modelo a utilizar para la edición de imágenes. | COMBO | Sí | `"FIBO"` |
| `image` | La imagen de entrada que deseas editar. | IMAGE | Sí | - |
| `prompt` | Instrucción para editar la imagen (predeterminado: vacío). | STRING | Sí | - |
| `negative_prompt` | Texto que describe lo que no deseas que aparezca en la imagen editada (predeterminado: vacío). | STRING | Sí | - |
| `structured_prompt` | Una cadena que contiene el prompt de edición estructurado en formato JSON. Úsala en lugar del prompt habitual para un control preciso y programático (predeterminado: vacío). | STRING | Sí | - |
| `seed` | Un número utilizado para inicializar la generación aleatoria, lo que garantiza resultados reproducibles (predeterminado: 1). | INT | Sí | 1 a 2147483647 |
| `guidance_scale` | Un valor más alto hace que la imagen siga el prompt más fielmente (predeterminado: 3.0). | FLOAT | Sí | 3.0 a 5.0 |
| `steps` | El número de pasos de eliminación de ruido que realizará el modelo (predeterminado: 50). | INT | Sí | 20 a 50 |
| `moderation` | Configuración de moderación. Al seleccionar `"true"` se muestran opciones de moderación adicionales para el contenido del prompt, la entrada visual y la salida visual. | DYNAMICCOMBO | Sí | `"false"`<br>`"true"` |
| `mask` | Si se omite, la edición se aplica a toda la imagen. | MASK | No | - |

**Restricciones importantes:**

- Debes proporcionar al menos una de las entradas `prompt` o `structured_prompt`. No pueden estar vacías ambas.
- Cuando el parámetro `moderation` se establece en `"true"`, aparecen tres entradas booleanas adicionales: `prompt_content_moderation` (predeterminado: false), `visual_input_moderation` (predeterminado: false) y `visual_output_moderation` (predeterminado: true).

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `IMAGE` | La imagen editada devuelta por la API de Bria. | IMAGE |
| `structured_prompt` | El prompt estructurado que se utilizó o generó durante el proceso de edición. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaImageEditNode/es.md)

---
**Source fingerprint (SHA-256):** `e66aaa563a82407408f25b289011a491c8b158822fc2db8912daf73731750081`
