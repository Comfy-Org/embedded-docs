# LTXVCropGuides

El nodo LTXVCropGuides procesa las entradas de condicionamiento y latentes para la generación de video, eliminando la información de fotogramas clave y ajustando las dimensiones del latente. Recorta la imagen latente y la máscara de ruido para excluir las secciones de fotogramas clave, mientras limpia los índices de fotogramas clave y las entradas de atención de guía de las entradas de condicionamiento positivas y negativas. Esto prepara los datos para flujos de trabajo de generación de video que no requieren guía por fotogramas clave.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `positivo` | La entrada de condicionamiento positivo que contiene información de guía para la generación. Sus índices de fotogramas clave determinan cuántos fotogramas se recortan del latente. | CONDITIONING | Sí | - |
| `negativo` | La entrada de condicionamiento negativo que contiene información de guía sobre qué evitar en la generación. Sus datos de fotogramas clave se limpian junto con el condicionamiento positivo. | CONDITIONING | Sí | - |
| `latente` | La representación latente que contiene muestras de imagen y datos de máscara de ruido. Cuando hay fotogramas clave presentes en el condicionamiento positivo, los últimos fotogramas clave se eliminan tanto de las muestras como de la máscara de ruido. | LATENT | Sí | - |

Nota: El recorte solo ocurre cuando el condicionamiento positivo contiene índices de fotogramas clave. Si no se detectan fotogramas clave, el condicionamiento positivo y negativo pasan sin cambios junto con el latente.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `positivo` | El condicionamiento positivo procesado con los índices de fotogramas clave y las entradas de atención de guía eliminadas | CONDITIONING |
| `negativo` | El condicionamiento negativo procesado con los índices de fotogramas clave y las entradas de atención de guía eliminadas | CONDITIONING |
| `latente` | La representación latente recortada con muestras y máscara de ruido ajustadas, donde se han eliminado las secciones de fotogramas clave | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVCropGuides/es.md)

---
**Source fingerprint (SHA-256):** `83e08bad281902e765ec18e06144b6a5fa730be2533932daa1d4076e6390b1e1`
