El nodo LTXVCropGuides procesa entradas de condicionamiento y latentes para la generación de video, eliminando información de fotogramas clave y ajustando las dimensiones latentes. Recorta la imagen latente y la máscara de ruido para excluir secciones de fotogramas clave, mientras limpia los índices de fotogramas clave tanto de las entradas de condicionamiento positivo como negativo. Esto prepara los datos para flujos de trabajo de generación de video que no requieren guía por fotogramas clave.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `positivo` | La entrada de condicionamiento positivo que contiene información de guía para la generación | CONDITIONING | Sí | - |
| `negativo` | La entrada de condicionamiento negativo que contiene información sobre qué evitar en la generación | CONDITIONING | Sí | - |
| `latente` | La representación latente que contiene muestras de imagen y datos de máscara de ruido | LATENT | Sí | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `positivo` | El condicionamiento positivo procesado con índices de fotogramas clave y entradas de atención guía limpiadas | CONDITIONING |
| `negativo` | El condicionamiento negativo procesado con índices de fotogramas clave y entradas de atención guía limpiadas | CONDITIONING |
| `latente` | La representación latente recortada con muestras y máscara de ruido ajustadas, donde se han eliminado las secciones de fotogramas clave | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVCropGuides/es.md)

---
**Source fingerprint (SHA-256):** `029309c260e09221cc9a046897589d99498f6e8ad984ef6052e50be9a0ea7b6d`
