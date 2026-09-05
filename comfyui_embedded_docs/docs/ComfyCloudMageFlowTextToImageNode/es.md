# ComfyCloudMageFlowTextToImageNode

Este nodo genera una imagen a partir de un prompt de texto enviando la solicitud al flujo de trabajo de texto a imagen Mage-Flow en Comfy Cloud. Ejecuta el paso de generación completo de 30 pasos en lugar del paso turbo destilado más rápido, y acepta un prompt negativo para que puedas describir contenido que no deseas en la imagen final. El prompt negativo es compatible con este modo de 30 pasos; según el resumen del nodo, la variante turbo destilada no puede aprovecharlo bien.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `prompt` | La descripción textual de la imagen a generar. | STRING | Sí | Texto libre |
| `negative_prompt` | Texto que describe el contenido que no debe aparecer en la imagen generada. Esta entrada se utiliza durante el paso de generación estándar de 30 pasos, pero la variante turbo destilada no utiliza bien los prompts negativos. | STRING | No | Texto libre |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `image` | La imagen generada a partir del prompt de texto y del prompt negativo proporcionados. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMageFlowTextToImageNode/es.md)

---
**Source fingerprint (SHA-256):** `80f4ecf1df3f2c46d94138f8ada817e12cc49e69e69a001630776ed644868367`
