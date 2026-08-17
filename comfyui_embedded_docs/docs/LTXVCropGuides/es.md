# LTXVCropGuides

El nodo LTXVCropGuides procesa entradas de condicionamiento y latentes para la generación de videos, eliminando información de keyframes y ajustando las dimensiones del latente. Recorta la imagen latente y la máscara de ruido para excluir las secciones de keyframes, a la vez que limpia los índices de keyframes tanto de las entradas de condicionamiento positivas como negativas. Esto prepara los datos para flujos de trabajo de generación de videos que no requieren guía de keyframes.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `positive` | La entrada de condicionamiento positivo que contiene información de guía para la generación | CONDITIONING | Sí | - |
| `negative` | La entrada de condicionamiento negativo que contiene información de guía sobre lo que se debe evitar en la generación | CONDITIONING | Sí | - |
| `latent` | La representación latente que contiene muestras de imagen y datos de máscara de ruido | LATENT | Sí | - |

Nota: Si el condicionamiento positivo no contiene índices de keyframes, el nodo devuelve las entradas positive, negative y latent sin cambios.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `positive` | El condicionamiento positivo procesado, con los índices de keyframes y las entradas de atención de guía eliminados | CONDITIONING |
| `negative` | El condicionamiento negativo procesado, con los índices de keyframes y las entradas de atención de guía eliminados | CONDITIONING |
| `latent` | La representación latente recortada con muestras y máscara de ruido ajustadas, donde se han eliminado las secciones de keyframes | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVCropGuides/es.md)

---
**Source fingerprint (SHA-256):** `83e08bad281902e765ec18e06144b6a5fa730be2533932daa1d4076e6390b1e1`
