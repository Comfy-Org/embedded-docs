> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVCropGuides/es.md)

El nodo LTXVCropGuides procesa entradas de condicionamiento y latentes para la generación de video, eliminando información de fotogramas clave y ajustando las dimensiones latentes. Recorta la imagen latente y la máscara de ruido para excluir secciones de fotogramas clave, mientras limpia los índices de fotogramas clave tanto de las entradas de condicionamiento positivo como negativo. Esto prepara los datos para flujos de trabajo de generación de video que no requieren guía por fotogramas clave.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `positivo` | CONDITIONING | Sí | - | La entrada de condicionamiento positivo que contiene información de guía para la generación |
| `negativo` | CONDITIONING | Sí | - | La entrada de condicionamiento negativo que contiene información sobre qué evitar en la generación |
| `latente` | LATENT | Sí | - | La representación latente que contiene muestras de imagen y datos de máscara de ruido |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `negativo` | CONDITIONING | El condicionamiento positivo procesado con índices de fotogramas clave y entradas de atención guía limpiadas |
| `latente` | CONDITIONING | El condicionamiento negativo procesado con índices de fotogramas clave y entradas de atención guía limpiadas |
| `latente` | LATENT | La representación latente recortada con muestras y máscara de ruido ajustadas, donde se han eliminado las secciones de fotogramas clave |

---
**Source fingerprint (SHA-256):** `029309c260e09221cc9a046897589d99498f6e8ad984ef6052e50be9a0ea7b6d`
